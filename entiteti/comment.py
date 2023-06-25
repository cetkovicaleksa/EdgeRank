from time import strftime, strptime
from konstante import DATE_FORMAT
from typing import Union

class Comment:
    def __init__(self, comment_list) -> None:

        (
            self.comment_id,
            self.status_id,
            self.comment_parent_id,
            self.comment_message,
            self.comment_author,
            self.date_commented,
            
            self.number_of_reactions,
            self.number_of_likes,
            self.number_of_loves,
            self.number_of_wows,
            self.number_of_hahas,
            self.number_of_sads,
            self.number_of_angrys,
            self.number_of_special
            
        ) = comment_list

        #self.date_commented = strptime(self.date_commented, DATE_FORMAT)



    @staticmethod
    def csv(comment: 'Comment', return_string: bool = True) -> Union[list, str]:
        ret = [
            comment.comment_id,
            comment.status_id,
            comment.comment_parent_id,
            comment.comment_message,
            comment.comment_author,
            strftime(DATE_FORMAT, comment.date_commented),
            
            comment.number_of_reactions,
            comment.number_of_likes,
            comment.number_of_loves,
            comment.number_of_wows,
            comment.number_of_hahas,
            comment.number_of_sads,
            comment.number_of_angrys,
            comment.number_of_special
        ]


        if return_string is True:
            ret = [str(val) for val in ret]
            ret = ",".join(ret) + '\n'

        return ret
