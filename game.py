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


#clear the game screen
def clear():
	if platform.system() =='Windows':
		os.system('cls')
	elif platform.system() == 'Linux':
		os.system('clear') 
	elif platform.system() == 'Darwin':
		os.system('clear')

#initialize global variables
player_name = ""
player_class = 0
player_health = 0
player_def = 0
player_atk = 0
player_pots = 0

#creates a new player and determines the stats based on the player class
def initPlayer(pname,pclass):
	global player_name
	player_name = pname
	global player_class
	player_class = pclass

	global player_health
	global player_def
	global player_atk

	#ninja
	if player_class==1:
		player_def = 4
		player_atk = 10
		player_health = 70
	#tank
	elif player_class==2:
		player_def = 15
		player_atk = 4
		player_health = 100
	#knight
	elif player_class==3:
		player_def = 7
		player_atk = 7
		player_health = 85
	#healer
	elif player_class==4:
		player_def = 4
		player_atk = 6
		player_health = 65

#prints the players stats and keep track of it
def player_stats():
	global player_name
	global player_class
	global player_health
	global player_def
	global player_atk

	print ("Name:", player_name)
	if player_class==1:
		print ("class: Ninja")
	#tank
	elif player_class==2:
		print ("class: Warrior")
	#knight
	elif player_class==3:
		print ("class: Knight")
	#healer
	elif player_class==4:
		print ("class: Priest")
	print ("Health:", player_health)
	print ("Armour:", player_def)
	print ("Damage:", player_atk)


clear()

#Global variable to center the text
columns = shutil.get_terminal_size().columns

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

#init global vairable room (the current game board)    
room = ""

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
				Gmap += "\'"
				Gmap += ch
				Gmap += "\',"
			Gmap = Gmap[:-5]
			Gmap+="]"
			Gmap+=","
	global room		
	exec("global room\n"
		"room = {"+Gmap[:-1]+"}")
movementAllowed = 1


#global variable position
pos = [] # 0 is X,1 is Y..ie [3,4] -> x=3, y=4


#clear and print data
def updater():
	if platform.system() =='Windows':
		os.system('cls')
	elif platform.system() == 'Linux':
		os.system('clear') 
	elif platform.system() == 'Darwin':
		os.system('clear')
	gamemap()
	player_pos()
	print()
	player_stats()


#print the game map
def gamemap():
	game_name()

	global columns
	for i in range(1,len(room)+1):
		toP = "".join(room[i])
		print(toP.center(columns))

def player_pos():
    for i in range(1,len(room)+1):
    	if stuff['player'] in room[i]:
    		x_axis = i
    		y_axis = room[i].index(stuff['player'])
    		global pos
    		del pos[:]
    		pos.append(x_axis)
    		pos.append(y_axis)


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


#controls the charcater movement
def movement():
	global room
	global pos
	global stuff
	global movementAllowed

	while movementAllowed == 0:
		pressedkey = getch()
		if pressedkey is 'w' or pressedkey is 'W':
			if room[pos[0]-1][pos[1]] is not stuff['wall_y'] and room[pos[0]-1][pos[1]] is not stuff['wall_x'] :
				up(room, stuff['empty'], stuff['player'])
				updater()
				print ("Location on Map", pos)
			else:
				print ("Bump! Wall : up")
		elif pressedkey is 's' or pressedkey is 'S':
			if room[pos[0]+1][pos[1]] is not stuff['wall_y'] and room[pos[0]+1][pos[1]] is not stuff['wall_x'] :
				down(room,stuff['empty'],stuff['player'])
				updater()
				print ("Location on Map", pos)
			else:
				print ("Bump! wall : down")
		elif pressedkey is 'a' or pressedkey is 'A':
			if room[pos[0]][pos[1]-1] is not stuff['wall_y'] and room[pos[0]][pos[1]-1] is not stuff['wall_x'] :
				left(room,stuff['empty'], stuff['player'])
				updater()
				print ("Location on Map", pos)
			else:
				print ("Bump! wall : left")
		elif pressedkey is 'd' or pressedkey is 'D':
			if room[pos[0]][pos[1]+1] is not stuff['wall_y'] and room[pos[0]][pos[1]+1] is not stuff['wall_x'] :
				right(room,stuff['empty'], stuff['player'])
				updater()
				print ("Location on Map", pos)
			else:
				print ("Bump! wall : right")
		elif pressedkey is 'x' or pressedkey is 'X':
			exit()


#start the game tutorial
def game_tutorial():
	scene("map_tutorial.txt")
	global movementAllowed
	movementAllowed=0
	updater()
	movement()



game_tutorial()





updater()

