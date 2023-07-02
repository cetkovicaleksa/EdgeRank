from time import strptime, strftime, struct_time
from typing import Union
from entiteti.person import Person
from entiteti.status import Status
from konstante import DATE_FORMAT


class Reaction:
    def __init__(self, reaction_list) -> None:
        self.status: Status = reaction_list[0]
        self.reaction_type: str = reaction_list[1]
        self.who_reacted: Person = reaction_list[2]
        self.date_reacted: struct_time = reaction_list[3]
        #self.date_reacted = strptime(reaction_list[3], DATE_FORMAT)


    @staticmethod
    def csv(reaction: 'Reaction', return_string: bool = True) -> Union[list, str]:
        ret = [
            reaction.status.status_id, reaction.reaction_type,
            reaction.who_reacted.person,
            strftime(DATE_FORMAT,reaction.date_reacted)
            ]
        return ','.join(ret) + '\n' if return_string else ret
    
