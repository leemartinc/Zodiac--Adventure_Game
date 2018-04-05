import os
import random
import platform
import shutil
import time
import random
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

room = ""

#clear the game screen
def clear():
	if platform.system() =='Windows':
		os.system('cls')
	elif platform.system() == 'Linux':
		os.system('clear') 
	elif platform.system() == 'Darwin':
		os.system('clear')

#prints the players stats and keep track of it
def player_stats():
	global player_name
	global player_class
	global player_health
	global player_def
	global player_atk
	global player_power
	global columns

	print()
	#print (":Name:".center(columns), player_name.center(columns))
	if player_class==1:
		print ("%s the Ninja".center(columns) % (player_name))
	#tank
	elif player_class==2:
		print ("%s the Warrior".center(columns) % (player_name))
	#knight
	elif player_class==3:
		print ("%s the Knight".center(columns) % (player_name))
	#healer
	elif player_class==4:
		print ("%s the Priest".center(columns) % (player_name))

	#stats = "Health: "% str(player_health)% "\tArmour: "% str(player_def)% "\tDamage: "% str(player_atk)

	#print(centerfy(stats), columns)

	print("Health: %s \tArmour: %s \t power: %s".center(columns) % (player_health, player_def, player_power))
	print()
	print("SKILLZ".center(columns))
	print(" sk1 max Damage: %s \t sk2 max Damage: %s \t sk3 Effect: %s".center(columns) % (player_skill1, player_skill2, player_skill3))

'''
	print (":Health:".center(columns) + str(player_health).center(columns))
	print()
	print (":Armour:".center(columns) + str(player_def).center(columns))
	print()
	print (":Damage:".center(columns) + str(player_atk).center(columns))
	'''

def monsterStats():
	global mon_char
	global mon_name
	global mon_health
	global mon_def
	global mon_attack
	#set monster global variables
	#to be called by gameCombat
	print("%s the Monster\t Health: %s".center(columns) % (mon_name, mon_health))

def player_pos():
    for i in range(1,len(room)+1):
    	if stuff['player'] in room[i]:
    		x_axis = i
    		y_axis = room[i].index(stuff['player'])
    		global pos
    		del pos[:]
    		pos.append(x_axis)
    		pos.append(y_axis)

#clear and print data
def updater():
	global w
	global statement
	global columns
	global combatAllowed
	clear()

	gamemap()
	player_pos()
	player_stats()
	if combatAllowed == 0:
		print()
		monsterStats()
	print()
	print()
	print()
	print(" INFO ".center(50, "#"))
	print (statement.center(50))
	print("".center(50, "#"))
	print()
	print()
	print()


def up(ditcioary,inst_replace,inst_player):
	(ditcioary[pos[0]]).pop(pos[1])
	(ditcioary[pos[0]]).insert(pos[1],inst_replace)
	(ditcioary[pos[0]-1]).pop(pos[1])
	(ditcioary[pos[0]-1]).insert(pos[1],inst_player)


def down(ditcioary,inst_replace,inst_player):
	(ditcioary[pos[0]]).pop(pos[1])
	(ditcioary[pos[0]]).insert(pos[1],inst_replace)
	(ditcioary[pos[0]+1]).pop(pos[1])
	(ditcioary[pos[0]+1]).insert(pos[1],inst_player)


def left(ditcioary,inst_replace,inst_player):
	(ditcioary[pos[0]]).pop(pos[1])
	(ditcioary[pos[0]]).insert(pos[1],inst_replace)
	(ditcioary[pos[0]]).pop(pos[1]-1)
	(ditcioary[pos[0]]).insert(pos[1]-1,inst_player)


def right(ditcioary,inst_replace,inst_player):
	(ditcioary[pos[0]]).pop(pos[1])
	(ditcioary[pos[0]]).insert(pos[1],inst_replace)
	(ditcioary[pos[0]]).pop(pos[1]+1)
	(ditcioary[pos[0]]).insert(pos[1]+1,inst_player)


#controls the charcater actions
def action():
	global room
	global pos
	global stuff
	global movementAllowed
	global statement
	global halt
	global combatAllowed

	while movementAllowed == 0:
		pressedkey = getch()
		specialPos()
		#function to test is play land on special pos
		#if specialfunction -- changes halt == 1:
			#if infoPos
				#function (change statement)
			#elif itemPos
				#function (adjust player stats)
			#elif combatPos
				#function (change chene)
		if pressedkey is 'w' or pressedkey is 'W':
			if room[pos[0]-1][pos[1]] is not stuff['wall_y'] and room[pos[0]-1][pos[1]] is not stuff['wall_x'] :
				up(room, stuff['empty'], stuff['player'])
				updater()
				print ("Location on Map:", pos)
			else:
				print ("Bump! Wall : up")
		elif pressedkey is 's' or pressedkey is 'S':
			if room[pos[0]+1][pos[1]] is not stuff['wall_y'] and room[pos[0]+1][pos[1]] is not stuff['wall_x'] :
				down(room,stuff['empty'],stuff['player'])
				updater()
				print ("Location on Map:", pos)
				
			else:
				print ("Bump! wall : down")
		elif pressedkey is 'a' or pressedkey is 'A':
			if room[pos[0]][pos[1]-1] is not stuff['wall_y'] and room[pos[0]][pos[1]-1] is not stuff['wall_x'] :
				left(room,stuff['empty'], stuff['player'])
				updater()
				print ("Location on Map:", pos)
				
			else:
				print ("Bump! wall : left")
		elif pressedkey is 'd' or pressedkey is 'D':
			if room[pos[0]][pos[1]+1] is not stuff['wall_y'] and room[pos[0]][pos[1]+1] is not stuff['wall_x'] :
				right(room,stuff['empty'], stuff['player'])
				updater()
				print ("Location on Map:", pos)
				
			else:
				print ("Bump! wall : right")
		elif pressedkey is 'p' or pressedkey is 'P':
			exit()
'''
	while combatAllowed == 0:
		pressedkey = getch()
		if pressedkey is '1':
			print("keyu 1")
		elif pressedkey is '2':
			print("keyu 2")
		elif pressedkey is '3':
			print("keyu 3")
		elif pressedkey is 'p' or pressedkey is 'P':
			exit()
'''
def centerfy(text, width=-1):
  lines = text.split('\n')
  width = max(map(len, lines)) if width == -1 else width
  return '\n'.join(line.center(width) for line in lines)

#initialize global variables
#Global variable to center the text
columns = shutil.get_terminal_size().columns
character = ""

player_name = ""
player_class = 0
player_health = 0
player_power = 0
player_def = 0
player_atk = 0
player_pots = 0
player_skill1 = 0
player_skill2 = 0
#skill 3 is class specific. conditional statement will be needed
player_skill3 = 0

mon_char = ""
mon_name = ""
mon_health = 0
mon_def = 0
mon_attack = 0

statement = ""
halt = 0
movementAllowed = 1
combatAllowed = 1
#global variable position
pos = [] # 0 is X,1 is Y..ie [3,4] -> x=3, y=4
#init global vairable room (the current game board)    
room = ""
specialStuff = {'tutCombatprompt': [10, 30],
				'tutMonster': [2, 41],
				'tutHealth': [2, 4],
				'tutEnd': [2, 53],
				'tutPortal': [11, 65],
				'mon1' : [38, 58],
				'mon2' : [29, 32],
				'mon3' : [25, 72],
				'mon4' : [11, 57],
				'mon5' : [33, 77],
				'mon6' : [19, 101],
				'mon7' : [30, 15],
				'mon8' : [13, 15],
				'mon9' : [4, 57],
				'monw' : [5, 114]}

#gets map from a text file in the game directory
#This takes each line and put it in the dictionary, set, list format....^^^^^^^^
def scene(file):
#build the map	
	global character	
	lineCounter = 1
	Gmap = ""
	with open(file) as f:
		for line in f:
			Gmap += str(lineCounter)
			Gmap += ":["
			lineCounter = lineCounter + 1
			for ch in line:
				if ch == "@":
					ch = character
				if ch == "%":
					ch = mon_char
				Gmap += "\'"
				Gmap += ch
				Gmap += "\',"
			Gmap = Gmap[:-5]
			Gmap+="]"
			Gmap+=","
	global room		
	exec("global room\n"
		"room = {"+Gmap[:-1]+"}")



class fightClub(object):
	global player_name
	global player_class
	global player_health
	global player_def
	global player_atk

	global mon_char
	global mon_name
	global mon_health
	global mon_def
	global mon_attack

	def __init__(self, name, HP, Damage, defense):
		self.name = name
		self.HP = HP
		self.Damage = Damage
		self.defense = defense

	def Battle(self, Opponent):
		global player_name
		global player_class
		global player_health
		global player_def
		global player_atk

		global mon_char
		global mon_name
		global mon_health
		global mon_def
		global mon_attack
		attackDamage = self.Damage - mon_def**(1/2)
		if attackDamage < 0:
			attackDamage = 0
		if (self.HP > 0):
			print("%s did %d Damage to %s"%(self.name, attackDamage, Opponent.name)) #Text-based combat descriptors
			print("%s has %d HP left"%(Opponent.name,Opponent.HP)) #Text-based descriptor for the opponent's health

			Opponent.HP -= attackDamage
			return Opponent.Battle(self)
		else:
			print("%s wins! (%d HP left)" %(Opponent.name, Opponent.HP)) #declares the winner of the Battle
			return Opponent, self

def fightClub2():
	global columns
	global combatAllowed
	global movementAllowed

	global player_name
	global player_class
	global player_health
	global player_def
	global player_atk
	global player_skill1
	global player_skill2
	global player_skill3
	global player_power

	global mon_char
	global mon_name
	global mon_health
	global mon_def
	global mon_attack


	p_health = player_health
	p_def = player_def
	p_atk = player_atk
	sk1 = player_skill1
	sk2 = player_skill2
	sk3 = player_skill3

	m_health = mon_health
	m_def = mon_def
	m_atk = mon_attack

	turn = 0
	error = 0
	attackDamage = 0

	while player_health > 0 and mon_health > 0:
		
		#player attack
		if turn == 0:
			updater()
			error = 0
			
			print("choose a skill".center(columns))
			pressedkey = getch()
			if pressedkey is '1':
				print("You selected skill 1")
				time.sleep(.5)
				attackDamage = random.randint(int(player_skill1-(player_skill1*.8)), int(player_skill1)) - (m_def**(.5))/2
				if attackDamage < 0:
					attackDamage = 0
					print("you did 0 damage to this monster.")
				mon_health -= attackDamage
				print("You just attacked with %s damage" % (attackDamage))
				time.sleep(2)
				turn = 1
			elif pressedkey is '2':
				if player_power > 1:
					print("You selected skill 2")
					time.sleep(.5)
					attackDamage = random.randint(int(player_skill2-(player_skill2*.8)), int(player_skill2)) - (m_def**(.5))/2
					if attackDamage < 0:
						attackDamage = 0
						print("you did 0 damage to this monster.")
					mon_health -= attackDamage
					print("You just attacked with %s damage but it took some power" % (attackDamage))
					time.sleep(2)

					player_power -= player_power*.3
					toSub = player_skill1/(player_power*.3)
					player_skill1 -= toSub

					turn = 1
				else:
					print("you do not have enough power for that skill")
					time.sleep(1)
			elif pressedkey is '3':
				#if condition for class
				if player_power > 1:
					#do stuff
					print("You have selected skill 3")
				else:
					print("you do not have enough power for that skill")
					time.sleep(1)
			elif pressedkey is 'p' or pressedkey is 'P':
				exit()
			elif pressedkey is not '1' or pressedkey is not '2' or pressedkey is not '3':
				error = 1
			if error == 1:
				print("invalid response")
		if turn == 1 and mon_health > 0:
			attackDamage = m_atk - p_def**(1/2)
			if attackDamage < 0:
				attackDamage = 0
			player_health -= attackDamage
			print("monster just attacked with %s damage" % (attackDamage))
			time.sleep(3)
			turn = 0

	combatAllowed = 1

	updater()
	if player_health > 0:
		print("player wins")
		player_power += mon_def*2
		p_health = player_health * (player_power*.6)
		player_health = int(p_health)
		mon_health = m_health
		time.sleep(3)
		player_skill1 = int(player_skill1 * (player_power*.8))
		prob = random.randint(5,9)
		player_skill2 = int(player_skill1 + player_skill1*(prob/10))
		print("Congratulations! Your stats have been improved")
	else:
		print("You died! GAME OVER!")
		time.sleep(5)
		exit()
	#scene("map.tutorial")

def gameCombat(monster):
	global specialStuff
	global mon_name
	global mon_health
	global mon_attack
	global mon_def
	global columns
	global movementAllowed
	global combatAllowed
	global player_name
	global player_health
	global player_def
	global player_atk
	#no WASD
	movementAllowed = 1
	combatAllowed = 0
	#arg will be monster position, and call specialStuff key....NVM...can just call specialStuff key name, no arg needed
	#function will handle switching scenes and actual key presses
	#monsterStats(update_stat)
	scene("map_combat.txt")
	updater()

	'''
	player = fightClub(player_name, player_health, player_atk, player_def)
	monster = fightClub(mon_name, mon_health, mon_attack, mon_def)
	Winner, Loser = player.Battle(monster)
	'''
	fightClub2()


	
	

def specialPos():
	global pos
	global statement
	global specialStuff
	global room

	global mon_char
	global mon_name
	global mon_health
	global mon_def
	global mon_attack
	global movementAllowed
	#######################################################################
	#Tutorial
	#Monster ahead
	if pos == specialStuff['tutCombatprompt']:
		statement="Monster ahead!\n\nYou can approch monster to\nstart the fight!\n\n Each fight will give you power that\nwill help you level up!"
	#monster fight
	if pos == specialStuff['tutMonster']:
		mon_char = "T"
		mon_name = "Tutorial Monster"
		mon_health = 10
		mon_def = 2
		mon_attack = 1
		gameCombat(specialStuff['tutMonster'])
	if pos == specialStuff['tutEnd']:
		statement="Thats all to it! \n Good luck warrior! \n\nHead to the portal to enter the game world!"
	if pos == specialStuff['tutPortal']:
		scene("map_world.txt")
		scene("map_world.txt")
	#######################################################################
	#Combat
	if pos == specialStuff['mon1']:
		mon_char = "1"
		mon_name = "Lerroooyyyy"
		mon_health = 67
		mon_def = 4
		mon_attack = 14
		gameCombat(specialStuff['mon1'])
		scene("map_world.txt")
		movementAllowed = 0
		gamemap()
		updater()
		action()

	


#creates a new player and determines the stats based on the player class
def initPlayer(pname,pclass):
	global player_name
	player_name = pname
	global player_class
	player_class = pclass

	global player_health
	global player_def
	global player_atk
	global player_skill1
	global player_skill2
	global player_skill3
	global player_power


	#ninja
	if player_class==1:
		player_def = 4
		player_skill1 =  10
		prob = random.randint(5,9)
		player_skill2 = int(player_skill1 + player_skill1*(prob/10))
		player_health = 70
		'''
		player_skill1 = 
		player_skill2 =
		#double damage
		player_skill3 = 
		'''
	#tank
	elif player_class==2:
		player_def = 15
		player_skill1 = 4
		prob = random.randint(5,9)
		player_skill2 = int(player_skill1 + player_skill1*(prob/10))
		player_health = 100
		player_skill3 = player_def*2
		'''
		player_skill1 = 
		player_skill2 =
		#double defense
		player_skill3 = 
		'''
	#knight
	elif player_class==3:
		player_def = 7
		player_skill1 = 7
		prob = random.randint(5,9)
		player_skill2 = int(player_skill1 + player_skill1*(prob/10))
		player_health = 85
		'''
		player_skill1 = 
		player_skill2 =
		#buff 
		player_skill3 = 
		'''
	#healer
	elif player_class==4:
		player_def = 4
		player_skill1 = 6
		prob = random.randint(5,9)
		player_skill2 = int(player_skill1 + player_skill1*(prob/10))
		player_health = 65
		player_skill3 = player_health/2
		'''
		player_skill1 = 
		player_skill2 = 
		#heal skill
		player_skill3 = 
		'''


clear()

#prints the name of the game..duhh
def game_name():
	file = open("game_name.txt") 
	lines = file.read().splitlines()
	for line in lines:
		print(line.center(columns))
	print()
	print()
game_name()

print()
print()

#asks user if they want to start the game
print("Start Game?".center(columns))
print("Y - START\tN - EXIT".center(columns))
#user's choice
begin = input()
#exits the game if "n" is selected
if begin == "n" or begin == "N":
	exit()

clear()
game_name()


#Character creation...used for init player function
print("CHARACTER CREATION".center(columns))
print()
print()
print()
print()
print("Enter a name for your Character:".center(columns))
print("**NOTE:Your character icon will be the".center(columns)) 
print("first letter of your character name!".center(columns))
print("It is Recommened you make the first letter UPPERCASE".center(columns))
player_name = input("Name: ")
character = player_name[:1]
print()
print()
print()
print()
print("Now lets Choose your Class!".center(columns))
print("There are FOUR classes to choose from".center(columns))
print("each with their own unique abilities".center(columns))
print()
print("1 - Ninja(Assassin)\tlow Defense\thigh Attack".center(columns))
print("2 - Warrior(Tank)\thigh Defense\tlow Attack".center(columns))
print("3 - Knight(Fighter)\tmid Defense\tmid Attack".center(columns))
print("4 - Priest(Healer)\tlow Defense\tmid Attack".center(columns))
#Makes sure only valid choices are selected
class_test = 1
while class_test == 1:
	try:
		player_class = eval(input("Class Number: "))
		if player_class < 1 or player_class > 4:
			print("invalid response...Try again")

		else:
			class_test = 0	
	except (SyntaxError, NameError, TypeError, ZeroDivisionError):
		pass
		print("invalid response...Try again")

initPlayer(player_name,player_class)


#changes the "@" to the player avatar
def insertPlayer(person):
	global room
	for i in range(1,len(room)+1):
		if room[i] == "@":
			room[i] = person
insertPlayer(character)	

#Global dictionary to describe the objects in the game environment
stuff = {'wall_y'  :  "|",
		'wall_x'  :  "=", 
		'player':  character,
		'empty' :  "·",
		'money' :  "$",
		'chest' :  "C"}	

    # data structure, dictionary...creating keyssss! DJ Khaled!!!
    #number in the left represent y axis and index of the lists is the x axis
"""room = {1:['┌','─','─','─','─','─','─','─','─','─','─','─','─','─','─','─','─','─','─','┐'],
		2:['│','·','·','·','·','·','·','·','·','·','·','·','·','·','·','·','·','·','·','│'],
		3:['│','·','·','·','·','·','·','·','·','·','·','·','·','·','·','·','·','·','·','│'],
		4:['│','·','·','·','·','·','·','·','·','·','·','·','·','·','·','·','·','·','·','│'],
		5:['│','@','·','·','·','·','·','·','·','·','·','·','·','·','·','·','·','·','·','│'],
		6:['└','─','─','─','─','─','─','─','─','─','─','─','─','─','─','─','─','─','─','┘']}"""


#controls what statments are printed on screen
def statement():
	global statement
	print(statement)




#print the game map
def gamemap():
	global room
	game_name()

	global columns
	for i in range(1,len(room)+1):
		toP = "".join(room[i])
		print(toP.center(columns))



#start the game tutorial + init game
def game_tutorial():
	global movementAllowed
	movementAllowed = 0
	scene("map_tutorial.txt")
	global statement
	statement = "This to the training area warrior!\n""Here you will learn how to complete you quest!\n\n""Lets start with movement.\n""Use W, A, S, D to move!"
	updater()
	action()



game_tutorial()
clear()
game_name()

def game_tutorial_aftCombat(file):
	scene("map_tutorial.txt")
	global character
	global movementAllowed
	global specialStuff
	lineCounter = 1
	Gmap = ""
	with open(file) as f:
		for line in f:
			Gmap += str(lineCounter)
			Gmap += ":["
			lineCounter = lineCounter + 1
			for ch in line:
				if ch == "@":
					ch = character
				if ch == "%":
					ch = mon_char
				if ch == "K":
					ch = "·"
				Gmap += "\'"
				Gmap += ch
				Gmap += "\',"
			Gmap = Gmap[:-5]
			Gmap+="]"
			Gmap+=","
	global room		
	exec("global room\n"
		"room = {"+Gmap[:-1]+"}")
	movementAllowed = 0
	combatAllowed = 1
	global statement
	statement = "You Defeated the monster!!!!\nCombat is pretty easy Right?\nJust dont die because Game over if you do!\n\nKeep Moving!"
	specialStuff['tutMonster'] = 0
	specialStuff['tutCombatprompt'] = 0
	gamemap()
	updater()
	#print("yolo")
	action()

game_tutorial_aftCombat("map_tutorial.txt")



