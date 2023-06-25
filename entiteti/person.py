from typing import Union, List, Set

class Person:
    def __init__(self, name: str, number_of_friends: int, friends: Set[str]) -> None:
        self.person: str = name
        self.number_of_friends: int = number_of_friends
        self.friends: Set[str] = friends

    def __hash__(self) -> int:
        return hash(self.person)

    @staticmethod
    def csv(person: 'Person', return_string: bool = True) -> Union[List[str], str]:
        frends: str = ','.join(frend for frend in person.friends)
        list_: List[str] = [person.person, str(person.number_of_friends), frends]

        return ','.join(list_) + '\n' if return_string else list_
