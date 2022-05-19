import os, sys

from util import _insert, _search

INV = {'name': [], 'location': {}, 'record': {}}
def insert():
	global INV
	_insert(INV)
	main()

def search():
	global INV
	search_term = raw_input()
	_search(INV, search_term)
	main()

def _exit():
	sys.exit()

def main():
	dct = { 1: 'insert()', 2: 'search()', 3: 'exit()'}
	print "1. insert\n2. search\n3. exit"
	option = int(raw_input("Enter option no: ").strip())
	if not dct.get(option):
		print "Invalid option! Choose any one from the below option"
		main()
	else:
		if option == 1:
			insert()
		if option == 2:
			search()
		else:
			_exit()

if __name__ == '__main__':
	main()