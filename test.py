import os
import random
import platform
import shutil
try:
    from msvcrt import getch #For windows
except ImportError: #For linux and maybe mac...
    #get the character pressed from the user
    def getch():
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

#key press function
def pressedkey():
	return getch()

class Pokemon(object):
    attackingDict = {'fire': {'fire': 0.5, 'grass': 2.0, 'water': 0.5}, 'grass': {'fire': 0.5, 'grass': 0.5, 'water': 2.0}, 'water': {'fire': 2.0, 'grass': 0.5, 'water': 0.5}}
    def __init__(self, name, HP, Damage, type):
        self.name = name     #Sets the name of the Pokemon
        self.HP = HP         #The Hit Points or health of this pokemon
        self.Damage = Damage #The amount of Damage this pokemon does every     attack
        self.type = type #Determines the type of the pokmeon to factor in effectiveness

    def Battle(self, Opponent):
        attackDamage = self.Damage * self.attackingDict[self.type][Opponent.type]

        if(self.HP > 0): #While your pokemon is alive it will coninute the Battle
            print("%s did %d Damage to %s"%(self.name, attackDamage, Opponent.name)) #Text-based combat descriptors
            print("%s has %d HP left"%(Opponent.name,Opponent.HP)) #Text-based descriptor for the opponent's health

            Opponent.HP -= attackDamage #The damage you inflict upon the opponent is subtracted here
            return Opponent.Battle(self)  #Now the Opponent pokemon attacks
        else:
            print("%s wins! (%d HP left)" %(Opponent.name, Opponent.HP)) #declares the winner of the Battle
            return Opponent, self  #return a tuple (Winner, Loser)


Squirtle = Pokemon('Squirtle', 100, 5, 'water')
Bulbasaur = Pokemon('Bulbasaur', 100, 10, 'grass')
Winner, Loser = Bulbasaur.Battle(Squirtle)
