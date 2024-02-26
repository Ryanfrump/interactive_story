from abc import ABC, abstractmethod
class Player:
    def __init__(self, name:str, starting_weapon:str, age:int) -> None:
        self.name = name
        self.starting_weapon = []
        self.age = age
        self.dictionary = dict()
        self.health = 100
        

    def take_damage(self, damage: int) -> None:
          self.health -= damage    
    @abstractmethod
    def ability(self, age: int):
        if 10<= age <=20:
            return "Your ability is swift! +2 to any dodge dice roll."
        elif 21<= age <=30:
            return "Your ability is enhanced combat! +2 to any attack."
        elif 31<= age <=10000000000000000000000000:
            return "Your ability is tank! +2 to Health."
        else:
            return "No age entered, please try again."
