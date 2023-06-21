from entiteti.status import Status
from typing import List, Dict, Union
from strukture.trie import Trie
import pickle



class TrieMap:
    
    
    @staticmethod
    def new_trie_map(statusi_lista: List[Status] = []) -> Dict[str, Trie]: 
        return { status.status_id : trie    for status, trie in (statusi_lista, Trie.new_trie_from_status(statusi_lista)) }
    
    
    #TODO:load and save trie_map
    @staticmethod
    def load_trie_map(path) -> Union[Dict[str, Trie], Dict, FileNotFoundError]:
        try:
            with open(path, "rb") as file:
                new_trie_map = pickle.load(file)
            return new_trie_map
        except FileNotFoundError:
            raise #temporary
        except EOFError:
            return TrieMap.new_trie_map()
            
        

    @staticmethod
    def save_trie_map(trie_map, path) -> Union[None, FileNotFoundError]:
        try:
            with open(path, "wb") as file:
                pickle.dump(trie_map, file)
        except FileNotFoundError:
            raise FileNotFoundError                 
