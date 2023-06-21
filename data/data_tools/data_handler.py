from data.data_tools.paths import Paths, PklPaths
from konstante import (
    FRIENDS_CSV, ORIGINAL_STATUSES_CSV, ORIGINAL_SHARES_CSV,
    ORIGINAL_COMMENTS_CSV, ORIGINAL_REACTIONS_CSV, 
    TEST_STATUSES_CSV, TEST_SHARES_CSV, TEST_COMMENTS_CSV,
    TEST_REACTIONS_CSV, TRIE_MAP_PKL, GRAPH_PKL
)
from data.data_tools.parse_files import *
from strukture.trie_map import TrieMap as tm 
import time



class DataHandler:
        
    __original_paths = Paths(FRIENDS_CSV, ORIGINAL_STATUSES_CSV, ORIGINAL_SHARES_CSV,
                           ORIGINAL_COMMENTS_CSV, ORIGINAL_REACTIONS_CSV)
    
    __test_paths = Paths(FRIENDS_CSV, TEST_STATUSES_CSV, TEST_SHARES_CSV,
                       TEST_COMMENTS_CSV, TEST_REACTIONS_CSV)
    
    __pkl_paths = PklPaths(TRIE_MAP_PKL, GRAPH_PKL)

    def __init__(self) -> None:
        pass

    
    
    def load_original_data(self):
        c = self
        return c.load_data(c.__original_paths.friends, c.__original_paths.statuses,
                             c.__original_paths.shares, c.__original_paths.comments, c.__original_paths.reactions)
        
    
    def load_test_data(self):
        c = self
        return c.__load_data(c.__test_paths.friends, c.__test_paths.statuses, 
                             c.__test_paths.shares, c.__test_paths.comments, c.__test_paths.reactions)


    @staticmethod
    def __load_data(friends_dir, statuses_dir, shares_dir, comments_dir, reactions_dir):
        pass




    @staticmethod
    def load_trie_map(path: str = None) -> tm:
        if not path:
            path = DataHandler.__pkl_paths.trie

        return tm.load_trie_map(path)

    @staticmethod
    def save_trie_map(trie_map: tm, path: str = None):
        if not path:
            path = DataHandler.__pkl_paths.trie

        tm.save_trie_map()


    @staticmethod
    def timed(*params, func: callable = lambda *args: None, loading_msg: str = None, end_msg: str = None):
        """Prints out a loading_msg and calls the passed func with given params.
        After the execution of given function prints out  the end_msg followed by the time it took to complete."""

        if loading_msg:
            print(loading_msg)
        
        timer = time.time()
        ret = func(*params) if params else func()
        timer = time.time() - timer
        if end_msg:
            print(end_msg, end='')

        print(timer)
        return ret



    