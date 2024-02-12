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
