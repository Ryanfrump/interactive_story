from abc import ABC, abstractmethod


class Player:
    def __init__(self, name:str, starting_object:str, age:int) -> None:
        self.name = name
        self.starting_object = []
        self.age = age
        self.dictionary = dict()

    @abstractmethod
    def ability(self,age:int):
        if 10<= age >=20:
            return "Your ability is flea! +2 to any flea dice roll."
        elif 21<= age >=30:
            return "Your ability is enhanced combat! +2 to any combat checks."
        elif 31<= age >=39:
            return "Your ability is enhanced intellect! +2 to any percesption roll."
        else:
            return "No age entered, please try again."
