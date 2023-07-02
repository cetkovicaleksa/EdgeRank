from collections import namedtuple
import itertools
from typing import Dict, NamedTuple, Union, Tuple, List, Set
from data.data_tools.stopwatch import StopwatchMessageMaker, StopwatchMaker
from konstante import ORIGINAL_PATHS, TEST_PATHS, PICKLE_PATHS, DATE_FORMAT
from data.data_tools.parse_files import (
    load_comments, load_reactions, load_shares, load_statuses, adjust_date_time,
    get_statuses_header, get_share_header, get_comment_header, get_reaction_header
)
from pretraga.affinity import make_affinity_graph
from strukture.trie_map import TrieMap as tm 
from strukture.trie import Trie
from strukture.graph import Graph

from entiteti.status import Status
from entiteti.comment import Comment
from entiteti.share import Share
from entiteti.reaction import Reaction
from entiteti.person import Person

import time
from time import strptime
import pickle




class DataHandler:
        
    __original_paths = ORIGINAL_PATHS
    
    __test_paths = TEST_PATHS
    
    __pkl_paths = PICKLE_PATHS

    class AllData(namedtuple("AllData", "data: Data trie: dict graph: Graph")):
            pass
    
    class Data(namedtuple("Data", "friends_dict statuses_dict statuses_list shares_list comments_list reactions_list")):
            pass

    def __init__(self) -> None:
        pass

    def __call__(self) -> AllData: #load all the data and pickled and return it
    
        data: DataHandler.Data = self.load_original_data()
        trie: Dict[str, Trie] = self.load_trie_from_default(data.statuses_list)
        graph: Graph = self.load_graph_from_default(data)
        return DataHandler.AllData(data, trie, graph)


    def load_original_data(self) -> Data:
        op = self.__original_paths
        backup = self.load_data
        timer = StopwatchMessageMaker(loading_msg=''.center(80, '=') + "\nLoading original data: :)\n", end_msg=''.center(80, '=')+"\nOriginal data loaded in: ")(self.load_data)
        ret = timer(op.friends, op.statuses, op.shares, op.comments, op.reactions)
        self.load_data = backup
        return ret        

    def load_test_data(self) -> Data:
        """
        Adjusts the dates of test data and then loads them.
        """
        tp = self.__test_paths
        StopwatchMessageMaker("Updating dates for test data...", "Dates updated in: ")(adjust_date_time)(tp.statuses, tp.comments, tp.shares, tp.reactions)

        data: DataHandler.Data = StopwatchMaker(DataHandler.load_data)(tp.friends, tp.statuses, tp.shares, tp.comments, tp.reactions, loading_msg = ''.center(80, '=') + "\nLoading test data: :)\n", end_msg = ''.center(80, '=')+"\nTest data loaded in: ")
        return data
    
    def load_trie_from_default(self, statusi_lista: List[Status] = []):
        return DataHandler.load_trie_map(self.__pkl_paths.trie, statusi_lista)
    
    def save_trie_to_default(self, trie_map):
        return DataHandler.save_trie_map(trie_map, self.__pkl_paths.trie)
    
    
    def load_graph_from_default(self, data: 'DataHandler.Data'):
        return DataHandler.load_graph(data, self.__pkl_paths.graph)
    
    def save_graph_to_default(self, graph):
        return DataHandler.save_graph(graph, self.__pkl_paths.graph)


    @staticmethod
    def load_data(
        friends_dir: str,
        statuses_dir: str,
        shares_dir: str,
        comments_dir: str,
        reactions_dir: str
        ) -> 'DataHandler.Data':        
        
        fren = DataHandler.load_friends(friends_dir)
        statuses_dict, statuses_list = DataHandler.load_statuses(fren, statuses_dir)
        shares = DataHandler.load_shares(fren, statuses_dict, shares_dir)
        comments = DataHandler.load_comments(fren, statuses_dict, comments_dir)
        reactions = DataHandler.load_reactions(fren, statuses_dict, reactions_dir)

        return DataHandler.Data(fren, statuses_dict, statuses_list, shares, comments, reactions)



    @staticmethod
    def load_trie_map(path: str, statusi_lista: List[Status] = []):
        return tm.load_trie_map(path, statusi_lista)

    @staticmethod
    def save_trie_map(trie_map: Dict[str, Trie], path: str):
        return tm.save_trie_map(trie_map, path)
    
    @staticmethod
    @StopwatchMessageMaker("-".center(80, '-')+"\n"+"Loading graph...", "Loaded graph in: ")
    def load_graph(data: 'DataHandler.Data', path: str) -> Graph:
        try:
            with open(path, "rb") as file:
                graph = pickle.load(file)
        except FileNotFoundError:
            graph = DataHandler.make_graph(data)
            with open(path, "wb") as file:
                pickle.dump(graph, file)
        return graph


    @staticmethod
    @StopwatchMessageMaker("Saving graph...", "Saved graph in: ")
    def save_graph(graph, path: str) -> Union[FileNotFoundError, None]:
        try:
            with open(path, "wb") as file:
                pickle.dump(graph, file)
        except FileNotFoundError:
            raise

    @staticmethod
    def make_graph(data: Data):
        return make_affinity_graph(data.friends_dict, data.statuses_dict, data.comments_list, data.shares_list, data.reactions_list) 

    @staticmethod
    def update_graph(original_graph: Graph, test_graph: Graph) -> Graph:
        ...

#-- loading and saving entities --


    @staticmethod
    @StopwatchMessageMaker("Loading friends...", "Friends loaded in: ")
    def load_friends(path: str) -> Dict[str, Person]: #person name : Person
        """Ucita in instancira sve prijatelje."""

        friends_friends: Dict[str, List[str]] = {} #maps person name to list of friend names
        friends_dict: Dict[str, Person] = {}  #maps person name to person object

        with open(path, 'r', encoding="utf-8") as file:
            for line in itertools.islice(file, 1, None):
                line = line.strip()
                row_list: List[str] = line.split(',')
                
                person, num_fren= row_list[:2]
                fren = row_list[2:]

                friends_friends[person] = fren
                friends_dict[person] = Person(person, num_fren)

        for friend in friends_dict.values():
            names_of_friends = friends_friends.pop(friend.person, [])
            friend.friends = set( friends_dict[friend_name] for friend_name in names_of_friends )


        return friends_dict
                        

    @staticmethod
    @StopwatchMessageMaker("Loading statuses...", "Statuses loaded in: ")
    def load_statuses(friends: Dict[str, Person], path: str) -> Tuple[Dict[str, Status], List[Status]]:
        statuses_dict: Dict[str, Status] = {}  

        def init(status_list):
            status_list[6:]: int = [ int(num) for num in status_list[6:]]
            status_list[4]: time.struct_time = strptime(status_list[4], DATE_FORMAT)
            status_list[5]: Person = friends[status_list[5]]

            status = Status(status_list)
            statuses_dict[status.status_id] = status
            return status

        statuses_list: List[Status] = [] 
        statuses_list.extend( init(status_list) for status_list in load_statuses(path) )
        return statuses_dict, statuses_list
    
    @staticmethod
    @StopwatchMessageMaker("Loading comments...", "Comments loaded in: ")
    def load_comments(friends: Dict[str, Person], statuses: Dict[str, Status], path: str) -> List[Comment]:
        comments_dict: Dict[str, Comment] = {}
        
        def init(comment_list):
            comment_list[1]: Status = statuses[comment_list[1]]
            comment_list[4]: Person = friends[comment_list[4]]
            comment_list[5]: time.struct_time = strptime(comment_list[5], DATE_FORMAT)
            comment_list[6:]: int = [ int(num) for num in comment_list[6:]]

            comment = Comment(comment_list)
            comments_dict[comment_list[0]] = comment
            return comment 
        

        comments_list: List[Comment] = []
        comments_list.extend( init(comment_list) for comment_list in load_comments(path) )
        
        for comment in comments_list:
            if comment.comment_parent:
                try:
                    comment.comment_parent = comments_dict[comment.comment_parent]
                except KeyError:
                    comment.comment_parent = ""  #temporary fix bc many comments don't have existing parent id
                    

        return comments_list

    @staticmethod
    @StopwatchMessageMaker("Loading shares...", "Shares loaded in: ")
    def load_shares(friends: Dict[str, Person], statuses: Dict[str, Status], path: str) -> List[Share]:
        def init(share_list):
            share_list[0]: Status = statuses[share_list[0]]
            share_list[1]: Person = friends[share_list[1]]
            share_list[2]: time.struct_time = strptime(share_list[2], DATE_FORMAT)
            return Share(share_list)
        
        shares: List[Share] = []
        shares.extend( init(share_list) for share_list in load_shares(path) )            
        return shares

    @staticmethod
    @StopwatchMessageMaker("Loading reactions...", "Reactions loaded in: ")
    def load_reactions(friends: Dict[str, Person], statuses: Dict[str, Person], path: str) -> List[Reaction]:
        def init(reaction_list):
            reaction_list[3]: time.struct_time = strptime(reaction_list[3], DATE_FORMAT)
            reaction_list[2]: Person = friends[reaction_list[2]]
            reaction_list[0]: Status = statuses[reaction_list[0]]
            return Reaction(reaction_list)
        
        reactions: List[Reaction] = []
        reactions.extend( init(reaction_list) for reaction_list in load_reactions(path) )
        return reactions
    

    @staticmethod
    def save_entity(entity_list: List[Union[Person, Status, Comment, Share, Reaction]], path: str) -> Union[None, FileNotFoundError]:
        try:
            clazz = type( next( iter(entity_list) ) )
        except StopIteration:
            raise ValueError("The provided list is empty!")
        
        if any( not isinstance(e, clazz) for e in entity_list ):
            raise ValueError(f"Not all entities in the provided list are the same type: [{clazz}]")

        headers = {
            Status : get_statuses_header, Share : get_share_header,
            Comment : get_comment_header, Reaction : get_reaction_header,
            Person : lambda: "person,number_of_friends,friends"
        }
        
        try:
            write_headers = headers[clazz]
        except KeyError:
            raise ValueError(f"Entity class is not supported. [{clazz}]")

        with open(path, 'w', encoding="utf-8", newline='') as file:
            file.write(write_headers() + "\n")
            for entity in entity_list:
                file.write(entity.csv(entity))

    

    









    # backup = (self.load_statuses, self.load_friends, self.load_comments, self. load_shares, self.load_reactions, self.load_data)
        # exception = None

        # DataHandler.load_statuses = StopwatchMessageMaker("Loading statuses...", "Loaded statuses in: ")(DataHandler.load_statuses)
        # DataHandler.load_friends = StopwatchMessageMaker("Loading friends...", "Loaded friends in: ")(DataHandler.load_friends)
        # DataHandler.load_comments = StopwatchMessageMaker("Loading comments...", "Loaded comments in: ")(DataHandler.load_comments)
        # DataHandler.load_shares = StopwatchMessageMaker("Loading shares...", "Loaded shares in: ")(DataHandler.load_shares)
        # DataHandler.load_reactions = StopwatchMessageMaker("Loading reactions...", "Reactions loaded in: ")(DataHandler.load_reactions)
        # DataHandler.load_data = StopwatchMessageMaker("Loading data: \n", "\nLoaded data in: ")(DataHandler.load_data)
        
        # try:
        #     ret = self.load_data(op.friends, op.statuses,
        #                          op.shares, op.comments, op.reactions)
        # except Exception as e:
        #     exception = e

        # DataHandler.load_statuses, DataHandler.load_friends, DataHandler.load_comments, DataHandler.load_shares, DataHandler.load_reactions, DataHandler.load_data = backup

        # if exception:
        #     raise exception
        
        # return ret