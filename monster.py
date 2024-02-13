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
    def __init__(self, name: str, damage: int, health: int) -> None:
        super().__init__(name = "goblin", damage = 1, health = 4)
        self.name = name
        self.damage = damage
        self.health = health
    

class Orc(Monster): pass 

class DireWolf(Monster): pass 

class Dragon(Monster): pass

class Hydra(Monster): pass
