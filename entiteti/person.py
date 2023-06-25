from typing import Union, List, Set

class Person:
    def __init__(self, name: str, number_of_friends: int, friends: Set[str]) -> None:
        self.name: str = name
        self.number_of_friends: int = number_of_friends
        self.friends: Set[str] = friends


    @staticmethod
    def csv(person: 'Person', return_string: bool = False) -> Union[List[str], str]:
        frends: str = ','.join(frend for frend in person.friends)
        list_: List[str] = [person.name, person.number_of_friends, frends]

        return ','.join(list_) if return_string else list_
