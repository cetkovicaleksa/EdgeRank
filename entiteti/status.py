from time import strptime, strftime, struct_time
from typing import Union
from entiteti.person import Person
from konstante import DATE_FORMAT

class Status:
    def __init__(self, status_list) -> None:

        (
            self.status_id,
            self.status_message,
            self.status_type,
            self.status_link,
            self.status_date_published, #datetime
            self.status_author,   #Person

            self.number_of_reactions,
            self.number_of_comments,
            self.number_of_shares,

            self.number_of_likes,
            self.number_of_loves,
            self.number_of_wows,
            self.number_of_hahas,
            self.number_of_sads,
            self.number_of_angrys,
            self.number_of_special

        ) = status_list

        self.status_id: str
        self.status_message: str
        self.status_type: str
        self.status_link: str
        self.status_date_published: struct_time
        self.status_author: Person

        self.number_of_reactions: int
        self.number_of_comments: int
        self.number_of_shares: int
        self.number_of_likes: int
        self.number_of_loves: int
        self.number_of_wows: int
        self.number_of_hahas: int
        self.number_of_sads: int
        self.number_of_angrys: int
        self.number_of_special: int
        #self.status_date_published = strptime(self.status_date_published, DATE_FORMAT)




    @staticmethod
    def csv(status: 'Status', return_string: bool = True) -> Union[list, str]:

        ret = [
            status.status_id,
            status.status_message,
            status.status_type,
            status.status_link,
            strftime(DATE_FORMAT, status.status_date_published),  
            status.status_author.person,

            status.number_of_reactions,
            status.number_of_comments,
            status.number_of_shares,
            
            status.number_of_likes,
            status.number_of_loves,
            status.number_of_wows,
            status.number_of_hahas,
            status.number_of_sads,
            status.number_of_angrys,
            status.number_of_special

        ]

        for i in range(6, len(ret)):
            ret[i] = str(ret[i])

        return ",".join(ret) + '\n' if return_string is True else ret
    

