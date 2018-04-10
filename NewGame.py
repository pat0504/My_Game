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
 
