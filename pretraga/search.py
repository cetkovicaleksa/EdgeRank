from strukture.trie_map import TrieMap as tm
from strukture.trie import Trie
from entiteti.status import Status
from typing import List



def search_score(*words: str, trie: Trie) -> int: #return the number of occurances of words in trie

    count = 0
    for word in words:
        count += trie.count_word_occurences(word)
    return count




def search(user: str, statuses_list: List[Status], trie_map: dict, affinity_graph: any) -> List[Status]:
    ...