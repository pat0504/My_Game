#This is Patrick's text base RPG adventure.
class Player:
    """ You are the player """

    def __init__(self, name, prof, maxhp, level, attack, defense = 5):
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
    

class Warrior(Player):
    def __init__(self):
        super().__init__(name = input("What is your characters name?"), prof = "Warrior", attack = 10, defense = 10,
                         maxhp = 100, level = 1)
        self.prof = "Warrior"
        self.maxhp = 100
        self.level = 1
    ####################### This is what I was in the middle of working on it.


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
        
#player_name = input("what is your name?")

#profession

x = Warrior()
print(x.prof)
