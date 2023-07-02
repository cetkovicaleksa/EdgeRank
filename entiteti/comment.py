from time import strftime, strptime, struct_time
from entiteti.status import Status
from konstante import DATE_FORMAT
from typing import List, Union

class Comment:
    def __init__(self, comment_list) -> None:

        (
            self.comment_id,
            self.status,
            self.comment_parent,
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

        self.comment_id: str
        self.status: Status
        self.comment_parent: Union[str, Comment]
        self.comment_message: str
        self.date_commented: struct_time

        self.number_of_reactions: int
        self.number_of_likes: int
        self.number_of_loves: int
        self.number_of_wows: int
        self.number_of_hahas: int
        self.number_of_sads: int
        self.number_of_angrys: int
        self.number_of_special: int

        #self.date_commented = strptime(self.date_commented, DATE_FORMAT)



    @staticmethod
    def csv(comment: 'Comment', return_string: bool = True) -> Union[List[str], str]:
        ret = [
            comment.comment_id,
            comment.status.status_id,
            comment.comment_parent.comment_id if isinstance(comment.comment_parent, Comment) else comment.comment_parent,
            comment.comment_message,
            comment.comment_author.person,
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

        for i in range(6, len(ret)):
            ret[i] = str(ret[i])
        
        return ",".join(ret) + '\n' if return_string is True else ret
