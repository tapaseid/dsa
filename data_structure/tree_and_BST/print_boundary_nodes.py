# Given a binary tree, print all boundary nodes

import pickle

class Node:
	def __init__(self, data=None):
		self.data = data
		self.left = None
		self.right = None


def printLeaves(root):
	if root:
		printLeaves(root.left)
		if root.left is None and root.right is None:
			print root.data,
		printLeaves(root.right)

def printBoundaryLeft(root):
	if root:
		if root.left:
			print root.data,
			printBoundaryLeft(root.left)
		elif root.right:
			print root.data,
			printBoundaryLeft(root.right)

def printBoundaryRight(root):
	if root:
		if root.right:
			printBoundaryRight(root.right)
			print root.data,
		elif root.left:
			printBoundaryRight(root.left)
			print root.data,

def printBoundary(root):
	if root:
		print root.data,
		printBoundaryLeft(root.left)
		printLeaves(root.left)
		printLeaves(root.right)
		printBoundaryRight(root.right)

def print_boundary_nodes(root, c=None, d=None):
	if not root:
		return

	if c is None:
		print_boundary_nodes(root.left, c=0, d='l')
		print root.data,
		print_boundary_nodes(root.right, c=1, d='r')

	if c == 0:
		print_boundary_nodes(root.right, c=0, d='r')
		print_boundary_nodes(root.left, c=0, d='l')
		
		if d == 'r' and root.right is None and root.left is None:
			print root.data,
		if d == 'l':
			print root.data,

	if c == 1:
		if d == 'l' and root.left is None and root.right is None:
			print root.data,
		if d == 'r':
			print root.data,

		print_boundary_nodes(root.right, c=1, d='r')
		print_boundary_nodes(root.left, c=1, d='l')

if __name__ == '__main__':
	with open("util/file", "r") as fh:
		root = pickle.load(fh)

	root.right.right = Node(7)
	root.right.left = Node(6)
	root.left.right.left = Node(9)
	print_boundary_nodes(root)
	print
	printBoundary(root)
