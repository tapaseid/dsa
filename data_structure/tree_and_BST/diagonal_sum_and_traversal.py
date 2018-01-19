# Print all diagonal sum
import pickle
from collections import defaultdict

INT_DICT = defaultdict(int)
LIST_DICT = defaultdict(list)

class Node:
	def __init__(self, data=None):
		self.left = None
		self.right = None
		self.data = data

def diagonal_sum(root, diagonal, d):
	if root is None:
		return
	d[diagonal] += root.data
	diagonal_sum(root.left, diagonal+1, d)
	diagonal_sum(root.right, diagonal, d)
	return d

def diagonal_traversal(root, diagonal, d_list):
	if root is None:
		return
	d_list[diagonal].append(root.data)
	diagonal_traversal(root.left, diagonal+1, d_list)
	diagonal_traversal(root.right, diagonal, d_list)
	return d_list

if __name__ == '__main__':
	with open("util/file", 'r') as f:
		root = pickle.load(f)
	root.right.left = Node(6)
	root.right.right = Node(7)

	d_int = diagonal_sum(root, 0, INT_DICT)
	for i in range(len(d_int)):
		print d_int[i]

	d_list = diagonal_traversal(root, 0, LIST_DICT)
	for i in range(len(d_list)):
		for j in d_list[i]:
			print j,
		print
