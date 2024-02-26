from abc import ABC, abstractmethod
from weapon import *
class Player:
    players = []
    
    def __init__(self, name: str, weapon: Weapon, age: int, health: int, damage: int) -> None:
        self.name = name
        self.age = age
        self.weapon = weapon
        self.dictionary = dict()
        self.health = health
        self.damage = damage
        
        Player.players.append(self)
        

    def take_damage(self, damage: int):
        Player.players[0].health -= damage
        print(f"{self} takes {damage} damage. Health is now {Player.players[0].health}.")   
    
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

