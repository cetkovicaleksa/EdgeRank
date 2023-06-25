from typing import List
from entiteti.status import Status
from strukture.trie import Trie
from strukture.trie_map import TrieMap
from data.data_tools.data_handler import DataHandler
from data.data_tools.stopwatch import StopwatchMaker
from konstante import ORIGINAL_PATHS, TEST_PATHS, MIXED_PATHS, PICKLE_PATHS





def main():
    dh = DataHandler()

    fren, statuses, shares, comments, reactions = dh.load_test_data()

    old_fren, old_statuses, old_shares, old_comments, old_reactions, old_trie, old_graph = dh()

    print('...')    
    new_statuses_list = statuses[0].extend(old_statuses[0])
    new_statuses_dict = statuses[1].extend(old_statuses[1])

    StopwatchMaker(dh.save_entity)(new_statuses_list, MIXED_PATHS.statuses, loading_msg = "Saving mixed statuses...", end_msg = "Saved in: ")
 
    print('...')
    new_trie = TrieMap.new_trie_map(statuses[0])
    old_trie.update(new_trie)
    TrieMap.save_trie_map(old_trie, PICKLE_PATHS.trie)


    ...



