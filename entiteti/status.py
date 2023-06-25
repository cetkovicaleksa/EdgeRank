from time import strptime, strftime
from typing import Union
from konstante import DATE_FORMAT

class Status:
    def __init__(self, status_list) -> None:

        (
            self.status_id,
            self.status_message,
            self.status_type,
            self.status_link,
            self.status_date_published,
            self.status_author,

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


        #self.status_date_published = strptime(self.status_date_published, DATE_FORMAT)




    @staticmethod
    def csv(status: 'Status', return_string: bool = False) -> Union[list, str]:

        ret = [
            status.status_id,
            status.status_message,
            status.status_type,
            status.status_link,
            strftime(DATE_FORMAT, status.status_date_published),  
            status.status_author,

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

        if return_string is True:
            ret = [str(val) for val in ret]
            ret = ",".join(ret) + '\n'

        return ret
    

