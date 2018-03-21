lineCounter = 1
Gmap = ""
room = {}
with open("test_map.txt") as f:
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


exec("room = {"+Gmap[:-1]+"}") 

print(room)

for i in range(1,len(room)+1):
	    print ("".join(room[i]))