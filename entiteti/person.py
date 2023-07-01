from typing import Union, List, Set

class Person:
    def __init__(self, name: str, number_of_friends: int = 0, friends: Set['Person'] = set()) -> None:
        self.person: str = name
        self.number_of_friends: int = number_of_friends
        self.friends: Set[Person] = friends

    def __hash__(self) -> int:
        return hash(self.person)
    

    @staticmethod
    def csv(person: 'Person', return_string: bool = True) -> Union[List[str], str]:
        list_: List[str] = [person.person, str(person.number_of_friends)]
        list_.extend( fren.person for fren in person.friends )

        return ','.join(list_) + '\n' if return_string else list_
