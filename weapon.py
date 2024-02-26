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


class RustySword(Weapon):
    def __init__(self) -> None:
        super().__init__(name= "Rusty Sword", damage= 3)

class RustyThrowingStar(Weapon):
    def __init__(self) -> None:
        super().__init__(name= "Throwing Star", damage= 3)

class RustyAxe(Weapon):
    def __init__(self) -> None:
        super().__init__(name= "Rusty Axe", damage= 3)

class RustyHalberd(Weapon):
    def __init__(self) -> None:
        super().__init__(name= "Rusty Halberd", damage= 3)

weapon_list = ["Rusty Halberd", "Rusty Axe", "Throwing Star", "Rusty Sword"]

        
