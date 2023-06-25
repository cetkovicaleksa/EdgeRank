from pretraga.edge_rank import edge_rank_score
from strukture.trie_map import TrieMap as tm
from strukture.trie import Trie
from strukture.graph import Graph
from entiteti.status import Status
from typing import List
from entiteti.person import Person
from konstante import SEARCH_WEIGHTS as sw





def words_count_score(*words: str, trie: Trie) -> int: #return the number of occurances of words in trie

    count = 0
    for word in words:
        count += trie.count_word_occurences(word)
    return count

def search_score(*words: str, status: Status, trie_map: tm, fren: Person, graph: Graph) -> float:
    ss = sw.word_weight * words_count_score(*words, trie =trie_map[status.status_id])
    es = 1 #edge_rank_score(status, fren, graph)
    return ss + sw.edge_rank_weight**es


def search(*words: str, fren: Person, statuses_list: List[Status], trie_map: dict, graph: Graph) -> List[Status]:
    return sorted( statuses_list, key=lambda status:search_score(*words, status = status, trie_map = trie_map, fren = fren, graph = graph), reverse = True )[:10]