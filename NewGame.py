 # Python Text Adventure RPG
 # Patrick's RPG

import cmd
import textwrap
import sys
import os
import time
import random

 screen_width = 100


 #### Player Setup #####
 class Player:
     def __init__(self):
         self.name = ''
         self.hp = 0
         self.mp = 0
myPlayer = player()

#### Title Screen ####
def title_screen_selections():
    options = input("> ")
    if option.lower() == ("play"):
        start_game() # placeholder until written
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        options = input("> ")
        if option.lower() == ("play"):
            start_game() # placeholder until written
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()

def title_screen():
    os.system('clear')
    print('-----------------------')
    print('| Welcome to my Game! |')
    print('-----------------------')
    print('        - Play -       ')
    print('        - Help -       ')
    print('        - Quit -       ')
    title_screen_selections()

def help_menu():
    print('-----------------------')
    print('| Welcome to my Game! |')
    print('-----------------------')
    print('- Use up, down, left, and right to move')
    print('- Type your commands to do them')
    print('- Good luck and have fun and do not die!')
    title_screen_selections()

#### GAME FUNCTIONALITY ####
def start_game():


#### VISUAL MAP ####
"""
 a1 a2 a3 a4
-------------
|  |  |  |  | a4
-------------
|  |  |  |  | b4
-------------
|  |  |  |  | c4
-------------
|  |  |  |  | d4
-------------
"""

DESCRIPTION = 'description'
EXAMINATION = 'examination'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {}
#### stopped at vid 3 6:04 ####








