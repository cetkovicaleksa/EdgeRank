import pickle
from time import strftime
from typing import List
from entiteti.person import Person
from entiteti.status import Status
from strukture.graph import Graph, IncomingDict
from strukture.trie import Trie
from strukture.trie_map import TrieMap
from data.data_tools.data_handler import DataHandler
from data.data_tools.stopwatch import StopwatchMaker
from konstante import DATE_FORMAT, ORIGINAL_PATHS, TEST_PATHS, MIXED_PATHS
import random
from pretraga.search import search
from pretraga.affinity import make_affinity_graph, establish_connections, make_friedship_graph
from pretraga.edge_rank import edge_rank_score

def login(frens: List[Person]):
    print("LOGIN".center(80, '='))
    print(''.center(80, '-'))
    print("Your name: ")
    username = input('>>')
    print(''.center(80, '-'))
    
    for fren in frens:
        if fren.person == username:
            return fren
        
    raise ValueError("Invalid username.")

def show_menu():
    print(''.center(80, '-'))
    print('2: view feed', '1: search', '0: exit', sep='\n')
    print(''.center(80, '-'))

    choice = input('>>')
    try:
        choice = int(choice)
        if choice in (0,1,2):
            return choice
        raise ValueError
    except ValueError as e:
        raise ValueError("Invalid choice.")

def cli():
    ...

if __name__ == "__main__":

    append_test_data: bool = False
    skip_login: bool = True

    
    dh = DataHandler()
    all_data: DataHandler.AllData = dh()

    trie_map: dict = all_data.trie
    graph: Graph = all_data.graph
    data: DataHandler.Data = all_data.data
    


    print('TRIE INFO'.center(80, '='))
    print("Number of tries: "+str(len(trie_map)))
    print(''.center(80, '='))
    
    print('GRAPH INFO'.center(80, '='))
    print("Vertex count: "+str(graph.vertex_count()), "Edge count: "+str(graph.edge_count()),"Default edge weight: "+str(graph.get_default_edge_weight()), sep='\n')
    print(''.center(80, '='))
    

    if append_test_data is True:
        
        test_friends = {person.person: person for person in graph.vertices()} #noob solution, the graph keeps Person objects as vertices and it also serializes them with itself, so when we first load the friends we make all their objects and after when we load the graph it loads its serialized Person objects so we have duplicates
        test_statuses_dict, test_statuses_list = dh.load_statuses(test_friends, TEST_PATHS.statuses)
        test_shares = dh.load_shares(test_friends, test_statuses_dict, TEST_PATHS.shares)
        test_comments = dh.load_comments(test_friends, test_statuses_dict, TEST_PATHS.comments)
        test_reactions = dh.load_reactions(test_friends, test_statuses_dict, TEST_PATHS.reactions)
        test_data = DataHandler.Data(test_friends, test_statuses_dict, test_statuses_list, test_shares, test_comments, test_reactions)

        test_trie_map: dict = TrieMap.new_trie_map(test_data.statuses_list)
        trie_map.update(test_trie_map)

        print("Updating graph...")        
        establish_connections(graph, test_data.friends_dict, test_data.statuses_dict, test_data.comments_list, 
                              test_data.shares_list, test_data.reactions_list)        

        
  
        #updating entity data
        data.friends_dict.update(test_data.friends_dict)
        data.comments_list.extend(test_data.comments_list)
        data.statuses_dict.update(test_data.statuses_dict)
        data.statuses_list.extend(test_data.statuses_list)
        data.reactions_list.extend(test_data.reactions_list)
        data.shares_list.extend(test_data.shares_list)

        print('NEW TRIE INFO'.center(80, '='))
        print("Number of tries: "+str(len(trie_map)))
        print(''.center(80, '='))
    
        print('NEW GRAPH INFO'.center(80, '='))
        print("Vertex count: "+str(graph.vertex_count()), "Edge count: "+str(graph.edge_count()),"Default edge weight: "+str(graph.get_default_edge_weight()), sep='\n')
        print(''.center(80, '='))

    

    if skip_login is True:
        user: Person = random.choice(list(data.friends_dict.values()))
    else:
        while 'LOGIN':
            try:
              user = login()
              break
            except ValueError as e:
                print(e)
                continue

    print("\nLogged in as: " + user.person)

    while 'LOGGED IN':
        try:
            choice = show_menu()
        except ValueError as e:
            print(e)
            continue

        if choice == 0:
            break

        if choice == 1:
            while 'Search':
                try:
                    c = input('Rijeci za pretragu ili 0 za nazad: >>').strip()
                    
                    if c == '0':
                        break

                    c = c.split()
                    result = search(*c, fren=user, statuses_list=data.statuses_list, trie_map=trie_map, graph=graph)
                   
                    for s in result:
                        print(''.center(80, '-'))
                        print(s.status_author.person, s.status_id, strftime(DATE_FORMAT, s.status_date_published), s.status_message, sep='\n')
                        print(''.center(80, '-'))

                except ValueError:
                    print("Molimo unesite rijeci u obliku: [word word word...]")
                except Exception:
                    break


        if choice == 2:
            result: List[Status] = sorted(data.statuses_list, key=lambda status: edge_rank_score(status, user, graph), reverse=True)[:10]
            for s in result:
                print(''.center(80, '-'))
                print(s.status_author.person, s.status_id, strftime(DATE_FORMAT, s.status_date_published), s.status_message, sep='\n')
                print(''.center(80, '-'))
  