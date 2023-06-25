from time import strftime
from typing import List
from entiteti.status import Status
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
    fren, statuses, shares, comments, reactions, trie, graph = dh()
    statusi_lista, statusi_rjecnik = statuses

    
    
    skip_login = True


    if skip_login:
        user = random.choice(fren)
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
                        print(s.status_author, s.status_id, strftime(DATE_FORMAT, s.status_date_published), s.status_message[:100] + '...', sep='\n')
                        print(''.center(80, '-'))
                    continue
                except ValueError:
                    print("Molimo unesite rijeci u obliku: [word word word...]")
                except Exception:
                    break


        if choice == 2:
            ...#show feed


