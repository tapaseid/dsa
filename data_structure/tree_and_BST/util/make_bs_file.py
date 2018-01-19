# Util module to create binary tree and write into a file for future use

import pickle

class Node:
	def __init__(self, data=None):
		self.left = None
		self.right = None
		self.data = data

if __name__ == '__main__':

	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)

	with open("file", "wb") as fh:
		pickle.dump(root, fh)
		