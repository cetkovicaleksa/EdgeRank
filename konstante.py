from entiteti.weights import *
from data.data_tools.paths import Paths, PklPaths


REACTION_WEIGHTS = RW = ReactionWeights(1, 2, 1.5, 1.5, 1.5, 1.5, 3)
STATUS_WEIGHTS = SW = StatusWeight(8, 6, 1)
HUMAN_INTERACTION_WEIGHTS = HIW = HumanInteractionWeights(17, 7, 5.7, 1)
SEARCH_WEIGHTS = SHW = SearchWeights(1500, 0, 0.3) 
TIME_DECAY_WEIGHTS = TDW = TimeDecayWeights(0.5, 18, 10, 7, 3, 2, 0.3) #decay rate and time threshold growth scaling

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

ORIGINAL_PATHS = OP = Paths(
    'data/dataset/friends.csv',
    'data/dataset/original_statuses.csv',
    'data/dataset/original_shares.csv',
    'data/dataset/original_comments.csv',
    'data/dataset/original_reactions.csv'
)

TEST_PATHS = TP = Paths(
    'data/dataset/friends.csv',
    'data/dataset/test_statuses.csv',
    'data/dataset/test_shares.csv',
    'data/dataset/test_comments.csv',
    'data/dataset/test_reactions.csv'
)

MIXED_PATHS = MP = Paths(
    'data/dataset/mixed_dataset/friends.csv',
    'data/dataset/mixed_dataset/mixed_statuses.csv',
    'data/dataset/mixed_dataset/mixed_shares.csv',
    'data/dataset/mixed_dataset/mixed_comments.csv',
    'data/dataset/mixed_dataset/mixed_reactions.csv'
)

PICKLE_PATHS = PP = PklPaths(
    'data/pickled/trie_map.pkl',
    'data/pickled/affinity_graph.pkl'
)


