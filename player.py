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
from player import Player
from monster import Monster
from weapon import Weapon

from abc import ABC, abstractmethod

class Monster(ABC):
    def __init__(self, name: str, damage: int, health: int, ) -> None:
        self.damage = damage
        self.health = health
        self.name = name


    @abstractmethod
    def monster_ability(self, name: str, damage: int) -> None:
        pass


class Goblin(Monster): pass

class Orc(Monster): pass 

class DireWolf(Monster): pass 

class Dragon(Monster): pass

class Hydra(Monster): pass

class Weapon:
    def __init__(self, name: str, damage: int) -> None:
        self.name = name    
        self.damage = damage
