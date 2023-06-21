from time import strptime, strftime
from typing import Union
from konstante import DATE_FORMAT

class Share:
    def __init__(self, share_list) -> None:
        self.status_id, self.who_shared = share_list[:2]
        self.date_shared = strptime(share_list[2], DATE_FORMAT)


    @staticmethod
    def csv(share: 'Share', return_string: bool = False) -> Union[list, str]:
        ret = [share.status_id, share.who_shared, strftime(DATE_FORMAT, share.date_shared)]
        return ','.join(ret) + '\n' if return_string else ret
        

