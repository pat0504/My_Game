Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
================== RESTART: C:\Pat_Rick\My_Game\NewGame6.py ==================
-----------------------
| Welcome to my Game! |
-----------------------
       - Play -       
       - Help -       
       - Quit -       
hello
Please enter a valid command.
> James
Please enter a valid command.
> Priest
Please enter a valid command.
> play
Please enter a valid command.
> Play
Please enter a valid command.
> Help
Please enter a valid command.
> 
================== RESTART: C:\Pat_Rick\My_Game\NewGame6.py ==================
-----------------------
| Welcome to my Game! |
-----------------------
       - Play -       
       - Help -       
       - Quit -       
>$>play
whatever
Hello, What is your name traveler? 

> James
Oh James is it?
What role would you like to play James
(Currently only warrior, priest, and mage are available)

================== RESTART: C:\Pat_Rick\My_Game\NewGame6.py ==================
-----------------------
| Welcome to my Game! |
-----------------------
       - Play -       
       - Help -       
       - Quit -       
>$>hello
Please enter a valid command.
> play
Please enter a valid command.
> jfkal
Please enter a valid command.
> 
================== RESTART: C:\Pat_Rick\My_Game\NewGame6.py ==================
-----------------------
| Welcome to my Game! |
-----------------------
       - Play -       
       - Help -       
       - Quit -       
>$>play
whatever
Hello, What is your name traveler? 

> Patrick
Oh Patrick is it?
What role would you like to play Patrick
(Currently only warrior, priest, and mage are available)

================== RESTART: C:\Pat_Rick\My_Game\NewGame6.py ==================
-----------------------
| Welcome to my Game! |
-----------------------
       - Play -       
       - Help -       
       - Quit -       
>$>play
whatever
Hello, What is your name traveler? 

> Patrick
Oh Patrick is it?
What role would you like to play Patrick
(Currently only warrior, priest, and mage are available)
> priest
You are now a priest

Hello, What is your name traveler? 
Welcome to this fantasy world of adventure!Let's hope you don't get too lost.Good luck.And have fun.Traceback (most recent call last):
  File "C:\Pat_Rick\My_Game\NewGame6.py", line 399, in <module>
    title_screen()
  File "C:\Pat_Rick\My_Game\NewGame6.py", line 51, in title_screen
    title_screen_selections()
  File "C:\Pat_Rick\My_Game\NewGame6.py", line 28, in title_screen_selections
    setup_game() # placeholder until written
  File "C:\Pat_Rick\My_Game\NewGame6.py", line 390, in setup_game
    os.sytem('clear')
AttributeError: module 'os' has no attribute 'sytem'
>>> 
================== RESTART: C:\Pat_Rick\My_Game\NewGame6.py ==================
-----------------------
| Welcome to my Game! |
-----------------------
       - Play -       
       - Help -       
       - Quit -       
>$>p
Please enter a valid command.
> play
Please enter a valid command.
> play
Please enter a valid command.
> quit
Please enter a valid command.
> 
Traceback (most recent call last):
  File "C:\Pat_Rick\My_Game\NewGame6.py", line 399, in <module>
    title_screen()
  File "C:\Pat_Rick\My_Game\NewGame6.py", line 51, in title_screen
    title_screen_selections()
  File "C:\Pat_Rick\My_Game\NewGame6.py", line 35, in title_screen_selections
    options = input("> ")
KeyboardInterrupt
>>> 
================== RESTART: C:\Pat_Rick\My_Game\NewGame6.py ==================
-----------------------
| Welcome to my Game! |
-----------------------
       - Play -       
       - Help -       
       - Quit -       
>$>play
whatever
Hello, What is your name traveler? 

> Patrick
Oh Patrick is it?
What role would you like to play Patrick
(Currently only warrior, priest, and mage are available)
> priest
You are now a priest

Hello, What is your name traveler? 
Welcome to this fantasy world of adventure!Let's hope you don't get too lost.Good luck.And have fun.################
# Let us begin #
################

==============================
What would you like to do?
> examine

==============================
What would you like to do?
> move

==============================
What would you like to do?
> 
