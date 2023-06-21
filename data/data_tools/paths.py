from collections import namedtuple



class Paths(namedtuple('Paths', 'friends statuses shares comments reactions')):
    pass
class PklPaths(namedtuple('PklPaths', 'trie graph')):
    pass