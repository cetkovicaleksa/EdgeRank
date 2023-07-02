from time import strptime, strftime, struct_time
from typing import Union
from entiteti.person import Person
from entiteti.status import Status
from konstante import DATE_FORMAT

class Share:
    def __init__(self, share_list) -> None:
        self.status: Status = share_list[0]
        self.who_shared: Person = share_list[1]
        self.date_shared: struct_time = share_list[2]
        #self.date_shared = strptime(share_list[2], DATE_FORMAT)


    @staticmethod
    def csv(share: 'Share', return_string: bool = True) -> Union[list, str]:
        ret = [
            share.status.status_id,
            share.who_shared.person,
            strftime(DATE_FORMAT, share.date_shared)
            ]
        return ','.join(ret) + '\n' if return_string else ret
        

