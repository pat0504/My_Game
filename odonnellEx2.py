#This is Patrick's text base RPG adventure.
class Player:
    """ You are the player """

    def __init__(self, name, maxhp=2, level=2, attack=2, defense = 5):
        self.name = name
        self.life = 1
        self.attack = attack
        self.defense = defense
        self.hp = 100
        self.xp = 0

    def level_up(self, level):
        while hero.xp >= Player.level2:
            pass
        
    def game_over(self):
        pass
    
    def death(self):
        if life >= 0:
            print("game_over")
        else:
            pass

class Mage(Player):
    pass
    # self.prof = "Mage"
    

class Warrior(Player):
    def __init__(self, name):
    #    self.prof = "Warrior"
        self.maxhp = 100
        self.level = 1
    
    self.prof = "Warrior"
    ####################### This is what I was in the middle of working on it.

class Odonnell(Player):
    pass


def profession():
    print("What is your class?",'\n',
          " press W for Warrior",'\n',
          " press M for Mage")
    pclass=input(">>>")
    if pclass == "W":
        Prof = Warrior()
    elif pclass == "M":
        Prof = Mage()

        #profession()
        
player_name = input("what is your name?")
player_prof = input("what is your profession -choose W or M- ?")
#profession

odonnell = Odonnell(player_name, 1, 2, 3, 4)
print(odonnell.name + "xxx")
if player_prof == 'W':
    x = Warrior(player_name)
    print(x.prof)
elif player_prof == 'M':
    x = Mage(player_name)
    x.prof = 'Mage'
    print(x.prof)
else:
    print('warning you have not created a play character')
