room = "k"

def scene(file):
#build the map		
	lineCounter = 1
	Gmap = ""
	with open(file) as f:
		for line in f:
			Gmap += str(lineCounter)
			Gmap += ":["
			lineCounter = lineCounter + 1
			for ch in line:
				Gmap += "\'"
				Gmap += ch
				Gmap += "\',"
			Gmap = Gmap[:-5]
			Gmap+="]"
			Gmap+=","
	global room		
	exec("global room\n"
		"room = {"+Gmap[:-1]+"}")

scene("test_map.txt")

#print (room)

for i in range(1,len(room)+1):
	    print ("".join(room[i]))
