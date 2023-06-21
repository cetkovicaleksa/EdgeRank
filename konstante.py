from entiteti.weights import *


REACTION_WEIGHTS = RW = ReactionWeights(1, 2, 1.5, 1.5, 1.5, 1.5, 3)
STATUS_WEIGHTS = SW = StatusWeight(8, 6, 0.5)
HUMAN_INTERACTION_WEIGHTS = HIW = HumanInteractionWeights(17, 7, 5.7, 1)

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

FRIENDS_CSV = 'data/dataset/friends.csv'

ORIGINAL_COMMENTS_CSV = 'data/dataset/original_comments.csv'
ORIGINAL_REACTIONS_CSV = 'data/dataset/original_reactions.csv'
ORIGINAL_SHARES_CSV = 'data/dataset/original_shares.csv'
ORIGINAL_STATUSES_CSV = 'data/dataset/original_statuses.csv'

TEST_COMMENTS_CSV = 'data/dataset/test_comments.csv'
TEST_REACTIONS_CSV = 'data/dataset/test_reactions.csv'
TEST_SHARES_CSV = 'data/dataset/test_shares.csv'
TEST_STATUSES_CSV = 'dataset/test_statuses.csv'

TRIE_MAP_PKL = 'data/pickled/trie_map.pkl'
GRAPH_PKL = 'data/pickled/affinity_graph.pkl'



