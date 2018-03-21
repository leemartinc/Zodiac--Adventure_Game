import numpy as np
from prettytable import PrettyTable

def main():
	
	x = createMap('test_map.txt')

	p = PrettyTable()

	for row in x:
		p.add_row(row)

	print (x)	

	print (p.get_string(header=False, border=False))


def createMap(file):
	contents = open(file).read()
	return [item.split() for item in contents.split('\n')[:-1]]

main()	

# map(str.split, open('test_map.txt'))