from typing import Dict, Union, Tuple, List, Set
from konstante import ORIGINAL_PATHS, TEST_PATHS, PICKLE_PATHS, DATE_FORMAT
from data.data_tools.parse_files import (
    load_comments, load_reactions, load_shares, load_statuses
)
from strukture.trie_map import TrieMap as tm 
from strukture.trie import Trie
from strukture.graph import Graph

from entiteti.status import Status
from entiteti.comment import Comment
from entiteti.share import Share
from entiteti.reaction import Reaction

import time
from time import strptime
import pickle




class DataHandler:
        
    __original_paths = ORIGINAL_PATHS
    
    __test_paths = TEST_PATHS
    
    __pkl_paths = PICKLE_PATHS

    def __init__(self) -> None:
        pass

    def __call__(self): #load all the data and pickled and return it
        ...
    
    def load_original_data(self):
        c = self
        return c.load_data(c.__original_paths.friends, c.__original_paths.statuses,
                             c.__original_paths.shares, c.__original_paths.comments, c.__original_paths.reactions)
        
    def load_test_data(self):
        ... #TODO: update dates with parse_files
        c = self
        return c.load_data(c.__test_paths.friends, c.__test_paths.statuses, 
                             c.__test_paths.shares, c.__test_paths.comments, c.__test_paths.reactions)
    
    
    def load_trie_from_default(self):
        return self.load_trie_map(self.__pkl_paths.trie)
    
    def save_trie_to_default(self, trie_map):
        return self.save_trie_map(trie_map, self.__pkl_paths.trie)
    
    def load_graph_from_default(self):
        return self.load_graph(self.__pkl_paths.graph)
    
    def save_graph_to_default(self, graph):
        return self.save_graph(graph, self.__pkl_paths.graph)


    @staticmethod
    def load_data(friends_dir, statuses_dir, shares_dir, comments_dir, reactions_dir):
        pass




    @staticmethod
    def load_trie_map(path: str, statusi_lista: List[Status] = []):
        return tm.load_trie_map(path, statusi_lista)

    @staticmethod
    def save_trie_map(trie_map: Dict[str, Trie], path: str):
        return tm.save_trie_map(trie_map, path)
    
    @staticmethod
    def load_graph(path: str) -> Graph:
        try:
            with open(path, "rb") as file:
                graph = pickle.load(file)
        except FileNotFoundError:
            graph = DataHandler.new_graph(...)
            with open(path, "wb") as file:
                pickle.dump(graph, file)
        return graph


    @staticmethod
    def save_graph(graph, path: str) -> Union[FileNotFoundError, None]:
        try:
            with open(path, "wb") as file:
                pickle.dump(graph, file)
        except FileNotFoundError:
            raise

    @staticmethod
    def new_graph() -> Graph:
        ...





    @staticmethod
    def load_friends(path: str) -> any:
        def load(path):
            ...

        def init(friends_list):
            ...

        return [ init(friends_list) for friends_list in load(path)]
        
        

    @staticmethod
    def load_statuses(path: str) -> Tuple[List[Status], Dict[str, Status]]:
        statuses_dict = {}   

        def init(status_list):
            status_list[6:]: int = [ int(num) for num in status_list[6:]]
            status_list[4]: time.struct_time = strptime(status_list[4], DATE_FORMAT)

            status = Status(status_list)
            statuses_dict[status.status_id] = status
            return status

        statuses_list = [ init(status_list) for status_list in load_statuses(path) ]

        return statuses_list, statuses_dict
    
    @staticmethod
    def load_comments(path: str) -> List[Comment]:
        def init(comment_list):
            comment_list[6:]: int = [ int(num) for num in comment_list[6:] ]
            comment_list[5]: time.struct_time = strptime(comment_list[5], DATE_FORMAT)
            return Comment(comment_list)
        
        return [ init(comment_list) for comment_list in load_comments(path) ]

    @staticmethod
    def load_shares(path: str) -> List[Share]:
        def init(share_list):
            share_list[2]: time.struct_time = strptime(share_list[2], DATE_FORMAT)
            return Share(share_list)

        return [ init(share_list) for share_list in load_shares(path)]

    @staticmethod
    def load_reactions(path: str) -> List[Reaction]:
        def init(reaction_list):
            reaction_list[3]: time.struct_time = strptime(reaction_list[3], DATE_FORMAT)
            return Reaction(reaction_list)

        return [ init(reaction_list) for reaction_list in load_reactions(path) ]
    
    #TODO: add saving for entities
    



    

    