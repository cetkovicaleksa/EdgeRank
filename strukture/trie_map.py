from entiteti.status import Status
from typing import List, Dict, Union
from strukture.trie import Trie
import pickle
from data.data_tools.stopwatch import StopwatchMaker, StopwatchMessageMaker



class TrieMap:
    
    
    @staticmethod
    @StopwatchMessageMaker("Making trie map...", "Made new trie map in: ")
    def new_trie_map(statusi_lista: List[Status] = []) -> Dict[str, Trie]: 
        trie_list = Trie.new_trie_from_status(*statusi_lista)
        dict_ = {}
        for i in range(len(statusi_lista)):
            dict_[statusi_lista[i]] = trie_list[i]
        return dict_
        #return { status.status_id : trie    for status, trie in (statusi_lista, Trie.new_trie_from_status(*statusi_lista)) }
    
    
    #TODO:load and save trie_map
    @staticmethod
    @StopwatchMessageMaker("-".center(80, '-')+"\n"+"Loading trie map...", "Loaded trie in: ")
    def load_trie_map(path, statusi_lista: List[Status] = []) -> Union[Dict[str, Trie], Dict]:
        try:
            with open(path, "rb") as file:
                new_trie_map = pickle.load(file)
            return new_trie_map
        except FileNotFoundError:
            tm = TrieMap.new_trie_map(statusi_lista)
            TrieMap.save_trie_map(tm, path)
            return tm
        

    @staticmethod
    @StopwatchMessageMaker("Saving trie map...", "Saved trie map in: ")
    def save_trie_map(trie_map, path) -> Union[None, FileNotFoundError]:
        try:
            with open(path, "wb") as file:
                pickle.dump(trie_map, file)
        except FileNotFoundError:
            raise                
