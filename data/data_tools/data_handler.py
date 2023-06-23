from typing import Union, Dict
from data.data_tools.paths import Paths, PklPaths
from konstante import (
    FRIENDS_CSV, ORIGINAL_STATUSES_CSV, ORIGINAL_SHARES_CSV,
    ORIGINAL_COMMENTS_CSV, ORIGINAL_REACTIONS_CSV, 
    TEST_STATUSES_CSV, TEST_SHARES_CSV, TEST_COMMENTS_CSV,
    TEST_REACTIONS_CSV, TRIE_MAP_PKL, GRAPH_PKL
)
from data.data_tools.parse_files import *
from strukture.trie_map import TrieMap as tm 
from strukture.trie import Trie
import time
import pickle



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
    def load_trie_map(path: str):
        return tm.load_trie_map(path)

    @staticmethod
    def save_trie_map(trie_map: Dict[str, Trie], path: str):
        return tm.save_trie_map(trie_map, path)
    
    # @staticmethod
    # def load_graph(path: str):
    #     pass

    # @staticmethod
    # def save_graph(graph, path: str):
    #     try:
    #         with open(path, "wb") as file:
    #             pickle.dump(graph, file)
    #     except FileNotFoundError:
    #         raise

    



    


    