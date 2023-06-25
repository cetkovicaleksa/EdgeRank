from entiteti.status import Status #nesto nije dobro?!
import re
from typing import Dict, List, Union


class Trie:

    __slots__ = "_root"

    class Node:
        __slots__ = "children", "num_of_repeats"
        
        def __init__(self, num_of_repeats = 0) -> None:
            self.children = {}      
            self.num_of_repeats = num_of_repeats



    def __init__(self) -> None:
        self._root = self.Node()


    def count_word_occurences(self, word: str) -> int:
        curr_node = self._root

        for char in word:
            curr_node = curr_node.children.get(char, None)

            if curr_node is None:
                return 0        

        return curr_node.num_of_repeats



    def add_word(self, word: str) -> None:

        curr_node = self._root
        for char in word:

            if char not in curr_node.children:
                curr_node.children[char] = Trie.Node()

            curr_node = curr_node.children[char]

        #ako je unjet prazan string poveca num_of_repeats za root(ili sprijeci ili moze biti korisno?!) 
        curr_node.num_of_repeats += 1


        # curr_node = self._root
        # for char in word:
        #     curr_node = curr_node.children.setdefault(char, Trie.Node())

        # curr_node.num_of_repeats += 1


    def add_words(self, *words: List[str]) -> None:
        word_cache: Dict[str, 'Trie.Node'] = {}

        for word in words:
            if word in word_cache:
                word_cache[word].num_of_repeats += 1
                continue

            curr_node = self._root #moze provjeriti ako je neka rijec iz word_cache prefiks trenutne pa da ne krece od root?
            for char in word:
                if char not in curr_node.children:
                    curr_node.children[char] = Trie.Node()

                curr_node = curr_node.children[char]
                

            curr_node.num_of_repeats += 1
            word_cache[word] = curr_node


        

    def __len__(self) -> int:
        return Trie.count_trie_nodes(self._root)

    @staticmethod
    def count_trie_nodes(starting_node: 'Trie.Node') -> int:
        
        if not starting_node: 
            return 0
        
        num_of_nodes = 1
        for node in starting_node.children.values():
            num_of_nodes += Trie.count_trie_nodes(node)
        return num_of_nodes
    

   
    @staticmethod 
    def new_trie_from_status(*statuses: Status) -> Union['Trie', List['Trie'], ValueError, AttributeError]:
        trie_list = []
        for status in statuses:
             # ukloni sve znakove osim brojeva, slova i razmaka (zadrzi prazan string?!?)
             # pretvori string u listu stringova
             message = [ re.sub(r'[^a-zA-Z0-9\s]', '', word) if word else word 
                        for word in status.status_message.split(' ') ]
             
             new_trie = Trie()
             new_trie.add_words(*message)
            #  for word in message: 
            #      new_trie.add_word(word)  #TODO: maby add function to add multiple words to trie?

             trie_list.append(new_trie)

        if len(trie_list) == 1:
            return trie_list[0]
        
        if len(trie_list) > 1:
            return trie_list
        
        raise ValueError("No statses provided!")
    