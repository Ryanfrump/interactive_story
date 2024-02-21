from player import Player
from monster import Monster, Goblin, DireWolf, Orc
from weapon import Weapon
import random

def func_path2(player):
    intro = f"""\
    Ahh yes...path 2...Welcome to this treacherous path, {player.name}, dream traveler. 
    The place where the air whispers of ancient tales,
    and every step echoes through the misty forest.
    
    The mystery of it is daunting. 
    What will you come across? 
    Or should I say who will you come across? 
    Where are you going?

    In the shadows of these towering mountains adventure awaits.
    And you will soon unlock all of these unknown secrets. 
    All I will say is it's going to be a guaranteed time to remember.
        
    {player.name}, your time is now. Choose your next move carefully:
    1. Venture deeper into the mountains... (Starting Weapon: Sword)
    2. Seek refuge in the nearby caves... (Starting Weapon: Wand)
    3. Travel underground mine route... (Starting Weapon: Bow)
    """

    print(intro)

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        print("\nYou choose to venture deeper into the mountains...")
        player.Weapon.append(Sword())
        encounter_monster(Player, Goblin())
    elif choice == "2":
        print("You decide to seek refuge in the nearby caves...")
        player.Weapon.append(Wand())
        encounter_monster(Player, DireWolf())
    elif choice == "3":
        print("You choose to travel the underground mine route...")
        player.Weapon.append(Bow())
        encounter_monster(player, Orc())
        
    else:
        print("Invalid choice! The journey ends here...")

    
    print("As you continue your journey, the path becomes more treacherous...")
    print("You hear ominous whispers in the wind, and the air grows colder.")


def encounter_monster(player, monster):
    print(f"You encounter a {monster.name}!")
    print("Prepare to defend yourself...")
    
    while player.health > 0 and monster.health > 0:
        player_attack_damage = player.attack()  # Implement player's attack method
        monster.take_damage(player_attack_damage)

        if monster.health <= 0:
            print(f"You defeated the {monster.name}!")
            break

        monster_attack_damage = monster.attack()  # Implement monster's attack method
        player.take_damage(monster_attack_damage)

        if player.health <= 0:
            print("You have been defeated...")
            break


if __name__ == "__main__":
    
    player = Player("Alice", 25)
    
    func_path2(player)





