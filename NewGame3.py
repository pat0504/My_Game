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
         self.job
         self.game_over = False
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

#### GAME INTERACTIVY ####
def print_location():
    print('/n' + ('#' +(4 * len(myPlayer.location))))
    print('#' + myPlayer.location.upper() + '#')
    print('#' + zonemap(myPlayer.position)[DESCRIPTION] + '#')
    print('/n' + ('#' +(4 * len(myPlayer.location))))

def prompt():
    print("/n" + "==============================")
    print("What would you like to do?")
    action = input(">")
    acceptable_actions =['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look']
    while action.lower() not in acceptable_actions:
        print("Unknown action, try again. /n")
        action = input("> ")
        if action.lower() == 'quite':
            sys.exit()
        elif action.lower() in ['move', 'go', 'travel', 'walk']:
            player_move(action.lower())
        elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
            player_examine(action.lower())

def player_move(myAction):
    ask = "Where would you like to move to?/n"
    dest = input(ask)
    if dest == ['up', 'north']:
        destination = zonemap[myPlayer.location][UP]
        movement_handler(destination)
    elif dest == ['left', 'west']:
          destination = zonemap[myPlayer.location][LEFT]
          movement_handler(destination)                 
    elif dest == ['right', 'east']:
          destination = zonemap[myPlayer.location][RIGHT]
          movement_handler(destination)
    elif dest == ['down', 'south']:
          destination = zonemap[myPlayer.location][DOWN]
          movement_handler(destination)


def movement_handler(destination):
    print("/n" = "You have moved to the " + destination + ".")
    myPlyaer.location = destination
    print_location()

def player_examine(action):
    if zonemap[myPlayer.location]:
        print("You have already exhausted this zone.")
    else:
        print("Trigger Puzzle here")
        

#### GAME FUNCTIONALITY ####
def start_game():
    return

def main_game_loop():
    while myPlayer.game_over = False:
    prompt()
    # here handle if puzzles have been solved, boss defeated, explored everything, etc.


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
ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examination'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False,                 
                 'c1': False, 'c2': False, 'c3': False, 'c4': False,
                 'd1': False, 'd2': False, 'd3': False, 'd4': False
                 }

zonemap = {
    'a1': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMINATION = 'examination'
        SOLVED = False
        UP = ''
        DOWN = 'b1'
        LEFT = ''
        RIGHT = 'a2'
    },
    'a2': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMINATION = 'examination'
        SOLVED = False
        UP = ''
        DOWN = 'b2'
        LEFT = 'a1'
        RIGHT = 'a3'
    },
    'a3': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMINATION = 'examination'
        SOLVED = False
        UP = ''
        DOWN = 'b3'
        LEFT = 'a2'
        RIGHT = 'a4'
    },
    'a4': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMINATION = 'examination'
        SOLVED = False
        UP = ''
        DOWN = 'b4'
        LEFT = 'a3'
        RIGHT = ''
    },
    'b1': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMINATION = 'examination'
        SOLVED = False
        UP = 'a1'
        DOWN = 'c1'
        LEFT = ''
        RIGHT = 'b3'
    },
    'b2': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMINATION = 'examination'
        SOLVED = False
        UP = 'a2'
        DOWN = 'c2'
        LEFT = 'b1'
        RIGHT = 'b3'
    },
    'b3': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMINATION = 'examination'
        SOLVED = False
        UP = 'a3'
        DOWN = 'c3'
        LEFT = 'b2'
        RIGHT = 'b4'
    },
    'b4': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMINATION = 'examination'
        SOLVED = False
        UP = 'a4'
        DOWN = 'c4'
        LEFT = 'b3'
        RIGHT = ''
    },
    'c1': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMINATION = 'examination'
        SOLVED = False
        UP = 'b1'
        DOWN = 'd1'
        LEFT = ''
        RIGHT = 'c2'
    },
    'c2': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMINATION = 'examination'
        SOLVED = False
        UP = 'b2'
        DOWN = 'd2'
        LEFT = 'c1'
        RIGHT = 'c3'
    },
    'c3': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMINATION = 'examination'
        SOLVED = False
        UP = 'b3'
        DOWN = 'd3'
        LEFT = 'c2'
        RIGHT = 'c4'
    },
    'c4': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMINATION = 'examination'
        SOLVED = False
        UP = 'b4'
        DOWN = 'd4'
        LEFT = 'c3'
        RIGHT = ''
    },
    'd1': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMINATION = 'examination'
        SOLVED = False
        UP = 'c1'
        DOWN = ''
        LEFT = ''
        RIGHT = 'd2'
    },
    'd2': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMINATION = 'examination'
        SOLVED = False
        UP = 'c2'
        DOWN = ''
        LEFT = 'd1'
        RIGHT = 'd3'
    },
    'd3': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMINATION = 'examination'
        SOLVED = False
        UP = 'c3'
        DOWN = ''
        LEFT = 'd2'
        RIGHT = 'd4'
    },
    'd4': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMINATION = 'examination'
        SOLVED = False
        UP = 'c4'
        DOWN = ''
        LEFT = 'd3'
        RIGHT = ''}
    }
def setup_game():
    os.system('clear')
################ Vid 4 3:11 ###################
    question1 = "


title_screen()


