from collections import namedtuple



class HumanInteractionWeights(namedtuple("HIWeights", "friends share comment reaction")):
    pass

class ReactionWeights(namedtuple("ReactionWeights", "likes loves wows hahas sads angrys special")):
    pass

class StatusWeight(namedtuple("StatusWeights", "shares comments reactions")):
    pass

class SearchWeights():
    pass


class TimeDecayWeights(namedtuple("TDWeights", "decay_factor last_hour today this_week this_month this_year long_time_ago")):
    pass

# class Treshold(namedtuple("Treshold", "criteria factor")):
#     pass



# class TimeDecayWeights(namedtuple("TDWeights", "decay_rate decay_tresholds")):
#     def __new__(cls, decay_rate: float, decay_thresholds: tuple):
#         class TimeDecayThresholds(namedtuple("TDTresholds", "last_hour today this_week this_month this_year long_time_ago")):
#             pass
#         class Threshold(namedtuple("Treshold", "criteria factor")):
#             pass

#         thresholds = [ Threshold(*threshold) for threshold in decay_thresholds ]
#         thresholds = TimeDecayThresholds(*thresholds)

#         return super().__new__(cls, decay_rate, thresholds)