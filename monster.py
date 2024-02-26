from abc import ABC, abstractmethod
class Monster(ABC):
    def __init__(self, name: str, damage: int, health: int, ) -> None:
        self.damage = damage
        self.health = health
        self.name = name
    
    def attack(self):
        print(f"{self.name} attacks for {self.damage} damage!")
        return self.damage
    
    def take_damage(self, damage: int):
        self.health -= damage
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")
    
    @abstractmethod
    def monster_ability(self, name: str, damage: int) -> None:
        pass





class Goblin(Monster):
    def __init__(self) -> None:
        super().__init__(name ="Goblin", damage =1, health =4)
    def monster_ability(self, name: str, damage: int) -> None:
        return super().monster_ability(name, damage)   
    

class Orc(Monster): 
    def __init__(self) -> None:
        super().__init__(name="Orc", damage=3, health=20)
    
    def monster_ability(self) -> None:
        return super().monster_ability(name="Hammer Smash", damage=5)


class DireWolf(Monster): 
    def __init__(self) -> None:
        super().__init__(name="Direwolf", damage=10, health=6)

    def monster_ability(self) -> None:
        return super().monster_ability(name="Quick Attack", damage=15)        

class Dragon(Monster): 
    def __init__(self) -> None:
        super().__init__(name="Dragon", damage=18, health=24)
    
    def monster_ability(self) -> None:
        return super().monster_ability(name="Flamethrower", damage=20)

class Hydra(Monster): 
    def __init__(self) -> None:
        super().__init__(name="Hydra", damage=36, health=72)

    def monster_ability(self) -> None:
        return super().monster_ability(name="Hyperbeam", damage=50)