from collections import namedtuple



class HumanInteractionWeights(namedtuple("HIWeights", "friends share comment reaction")):
    pass

class ReactionWeights(namedtuple("ReactionWeights", "likes loves wows hahas sads angrys special")):
    pass

class StatusWeight(namedtuple("StatusWeights", "share comment reactions")):
    pass

class SearchWeights():
    pass
