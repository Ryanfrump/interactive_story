from player import Player
from monster import Monster
from weapon import Weapon
import random
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
    
    Oh yes by the way please chose a weapon dont want to make it to unfair """
    
    
    
    
    
    
    
    
    
    
    
    
    print(intro)
    first_choice = input("Will you fight or flee?: ")
    if first_choice == "flee":
        print(first_choice_flee)
    elif first_choice == "fight":
        print(first_choice_fight)
        print(Weapon.weapon_list())




