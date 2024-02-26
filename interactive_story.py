from player import Player
from weapon import *
import path1
import path2




player_name = input("What is your name?: ")
player_age = int(input("What is your age?: "))



welcome_message = f"""Welcome {player_name}! To your dream world! 
Based on your age {player_age}, your special ability is {Player.ability(Player, player_age)}


inside here, you will be able to choose 1 of 2 paths.
You have your path1 and path2...
"""
print(welcome_message)
path_choice = input("Which path will you chose path1 or path2?: ")
if path_choice == "path1":
    weapon_choice_input = input(f"Choose your weapon {', '.join(weapon_options.keys())}: ").lower()
    weapon_class = weapon_options.get(weapon_choice_input)
    character = Player(player_name, weapon_class, player_age, 100, 3)
    path1.func_path1()
elif path_choice == "path2":
    path2.func_path2()
else:
    print("Not a path")

