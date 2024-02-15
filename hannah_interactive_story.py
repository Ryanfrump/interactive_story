from abc import ABC, abstractmethod

class GameObject(ABC)
    abstractmethod
    def use(self)
        pass
class Player:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.inventory= []
        self.age = age
        self.health = 100
    
    def take_damage(self, damage: int) -> None:
        self.health -= damage

    @abstractmethod
    def ability(self,age: int):
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


class Goblin(Monster):
    def monster_ability(self, player: Player) -> None:
        player.take_damage(self.damage)
        pass

class Orc(Monster): pass 

class DireWolf(Monster): pass 

class Dragon(Monster): pass

class Hydra(Monster): pass

class Weapon:
    def __init__(self, name: str, damage: int) -> None:
        self.name = name    
        self.damage = damage
