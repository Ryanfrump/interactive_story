from player import *
from monster import *
from weapon import *


def func_path1():
    intro = """Ahh yes so i see you have chosen path 1 that is quite bold of you
if i do say myself!!

Where are you, you might ask, well i know your scared but if you would open
your eyes you would be quick to find out!

Realising your eyes have been closed this whole time you open them
and see yourself surrounded by thousands of cheering people
in what seems to be a giant colosseum

From the top of the colosseum you see a man emerge from a dark room
and he says a yes you have awoken!

You are our main event and will be fighting the gauntlet of monsters"""
    
    first_choice_flee = "Suddenly you wake up to find this was all a dream congratulations your lame!!"
    first_choice_fight = """So I see we have found a warrior, you will now be faced with the gauntlet
which will include a series of 5 fight good luck warrior we will be watching from above. 
your first fight will be against a goblin lets see what you can do"""
    first_win = """Congrats you have beat you first opponent not that i was expecting you
to lose anyways its just a goblin after all

your next opponent is gonna be a little tougher this time so you dont
get bored to early! it will be a Orc have fun bud!!!"""
    second_win = """It looks like you were able to defeat the orc also
good job you did a little bit better than i expected 

your next opponent wont be as beefy as the orc but it packs a little
bit more of a punch so have fun with this dire wolf try not to 
die on us if you could im just starting to get entertained here"""
    third_win = """Wow kinda surprising me here didnt think you were
gonna get passed that one but good job you earned that one.

this is gonna be the end of the road for you though because for this fight were
bringing out the baddie of the sky donkneys one true lover THE DRAGON!!!!!!!"""
    
    
    
    
    
    
    print(intro)
    first_choice = input("Will you fight or flee?: ").lower()

    if first_choice == "flee":
        print(first_choice_flee)
    elif first_choice == "fight":
        print(first_choice_fight)

    # List of monsters to fight in order
        monsters_to_fight = [Goblin(), Orc(), DireWolf(), Dragon()]
        player_character = Player.players[0]  

        for monster in monsters_to_fight:
            while Player.players[0].health > 0 and monster.health > 0:
                print(f"Fighting {monster.name}...")
                monster.take_damage(player_character.damage)  # Player attacks monster
                if monster.health <= 0:
                    print(f"{monster.name} has been defeated!\n")
                # Break if last monster has been defeated, or continue to the next monster
                    if monster == monsters_to_fight[-1]:
                        print("All monsters have been defeated! You win!")
                    continue
            
                Player.take_damage(Player.players[0].name, monster.damage)  # Monster attacks player
                if Player.players[0].health <= 0:
                    print(f"{Player.players[0].name} has been defeated!")
                    break  # Exit the loop if the player is defeated
        
            if Player.players[0].health <= 0:
                break  # Break the outer loop if the player is defeated
        




