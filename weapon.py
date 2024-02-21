class Weapon:
    def __init__(self, name: str, damage: int) -> None:
        self.name = name
        self.damage = damage

class Sword(Weapon):
    def __init__(self) -> None:
        super().__init__(name="Sword", damage=10)

class Wand(Weapon):
    def __init__(self) -> None:
        super().__init__(name="Wand", damage=8)

class Bow(Weapon):
    def __init__(self) -> None:
        super().__init__(name="Bow", damage=12        



        
