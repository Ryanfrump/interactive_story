from player import Player
from monster import Monster



player_name = input("What is your name?: ")
player_age = int(input("What is your age?: "))
character = Player(player_name, player_age, "Sword")


welcome_message = f"""Welcome {player_name}! To your dream world! 
Based on your age {player_age}, your special ability is {Player.ability(Player, player_age)}


inside here, you will be able to choose 1 of 2 paths.
You have your path1 and path2...
"""
print(welcome_message)
path_choice = input("Which path will you chose path1 or path2?: ")
print(path_choice)
if path_choice == "path1":
    print("yay")
elif path_choice == "path2":
    print("almost yay")
else:
    print("Not yay")

