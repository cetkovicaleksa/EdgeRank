from time import strptime, strftime
from typing import Union
from konstante import DATE_FORMAT


class Reaction:
    def __init__(self, reaction_list) -> None:
        self.status_id, self.reaction_type, self.who_reacted, self.date_reacted = reaction_list #reaction_list[:3]
        #self.date_reacted = strptime(reaction_list[3], DATE_FORMAT)


    @staticmethod
    def csv(reaction: 'Reaction', return_string: bool = False) -> Union[list, str]:
        ret = [reaction.status_id, reaction.reaction_type, reaction.who_reacted, strftime(DATE_FORMAT, reaction.date_reacted)]
        return ','.join(ret) + '\n' if return_string else ret
    
