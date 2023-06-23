from entiteti.status import Status
from strukture.trie import Trie
from strukture.trie_map import TrieMap
from data.data_tools.data_handler import DataHandler
from data.data_tools.stopwatch import StopwatchMaker
import time

@StopwatchMaker #('something', loading_msg='...', end_msg='Loaded in: ')
def main(*something):
    time.sleep(5)
    print(something)
    return "Hello World!"


if __name__ == "__main__":
    print(main)
    #main('something')
    print(main)
    # status_list = [
    # "12345",
    # "Hello, Hello Help hello world world!",
    # "Type",
    # "https://example.com",
    # "2022-01-01 12:34:56",
    # "John Doe",
    # 100,
    # 50,
    # 20,
    # 70,
    # 10,
    # 5,
    # 3,
    # 2,
    # 1,
    # 8
    # ]

    
    

    # status = Status(status_list)
    # status.status_message = "900 "*1000#"Thism new evidence could very well elect Trump.IT'S OVER: Wikileaks Exposes The Assassination Of Scalia... This Will Bring Down The Clintons And The Democratic Party!"

    # # dh = DataHandler()
    # # try:
    # #     trie = dh.timed(dh.load_original_data, loading_msg="Loading...", end_msg=" ")
    # # except Exception:
    # #     raise
    # # except TypeError:
    # #     raise
    # trie = DataHandler.timed(Trie.new_trie_from_status, status)    
    # print(trie)
    # #trie = Trie.new_trie_from_status(status)

    # print(status.csv(status, True))
    # #print(len(trie))


    
    # trie.add_word("90")
    # #print(len(trie))
    
    # print(trie.count_word_occurences('900'))

