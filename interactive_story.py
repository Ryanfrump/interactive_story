from player import Player
import path1
import path2



player_name = input("What is your name?: ")
player_age = int(input("What is your age?: "))
weapon_choice = 
character = Player(player_name, player_age, )


welcome_message = f"""Welcome {player_name}! To your dream world! 
Based on your age {player_age}, your special ability is {Player.ability(Player, player_age)}


inside here, you will be able to choose 1 of 2 paths.
You have your path1 and path2...
"""
print(welcome_message)
path_choice = input("Which path will you chose path1 or path2?: ")
if path_choice == "path1":
    path1.func_path1()
elif path_choice == "path2":
    path2.func_path2()
else:
    print("Not a path")

