import pickle
from time import strftime
from typing import List
from entiteti.status import Status
from strukture.graph import IncomingDict
from strukture.trie import Trie
from strukture.trie_map import TrieMap
from data.data_tools.data_handler import DataHandler
from data.data_tools.stopwatch import StopwatchMaker
from konstante import DATE_FORMAT, ORIGINAL_PATHS, TEST_PATHS, MIXED_PATHS
import random
from pretraga.search import search

def login(frens):
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



if __name__ == "__main__":
    
    dh = DataHandler()

    # graph = dh.load_graph_from_default(None)
    
    data: DataHandler.AllData = None
    graph = dh.load_graph_from_default(None)

    iter = next(iter(graph._adj.items()))
    print(type(iter[1]))
    print(iter[1]["aki"],type(iter[1]), iter[1].get_default_value())
    print(type(graph._adj["aki"]))
    print(type(graph._adj))
    print(graph.vertex_count())
    print(graph.edge_count())
    iter = ( (x.person, x.number_of_friends) for x in graph.vertices())
    
    print('...')
    while(True):
        print(next(iter))
        raise KeyboardInterrupt()
    
    
    skip_login = True


    if skip_login:
        user = random.choice(list(data.friends_dict.values()))
    else:
        while 'LOGIN':
            try:
              user = login()
              break
            except ValueError as e:
                print(e)
                continue
        
    print('Logged in as: ' + user.person)
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
                    result = search(*c, fren=user, statuses_list=statusi_lista, trie_map=trie, graph=None)
                    for s in result:
                        print(''.center(80, '-'))
                        print(s.status_author, s.status_id, strftime(DATE_FORMAT, s.status_date_published), s.status_message[:1000] + '...', sep='\n')
                        print(''.center(80, '-'))
                    continue
                except ValueError:
                    print("Molimo unesite rijeci u obliku: [word word word...]")
                except Exception:
                    break


        if choice == 2:
            ...#show feed


