# Need to print all nodes which can be seen from the top of a tree

import pickle

class Node:
	def __init__(self, data=None):
		self.data = data
		self.left = None
		self.right = None

def top_view(root):
	if not root:
		return

	arr = []
	arr.append(root.data)
	left_c = root.left
	right_c = root.right

	while left_c or right_c:
		if left_c:
			arr.insert(0, left_c.data)
			left_c = left_c.left

		if right_c:
			arr.append(right_c.data)
			right_c = right_c.right

	return arr

def top_view_recursion(root, pos=None):
	if not root:
		return
	
	if pos is None:
		top_view_recursion(root.left, 0)
		print root.data,
		top_view_recursion(root.right, 1)

	if pos == 0:
		top_view_recursion(root.left, 0)
		print root.data,

	if pos == 1:
		print root.data,
		top_view_recursion(root.right, 1)


if __name__ == '__main__':
	with open("util/file", "r") as fh:
		root = pickle.load(fh)

	root.right.right = Node(7)
	root.right.left = Node(6)
	root.left.right.left = Node(9)
	print top_view(root)

	top_view_recursion(root)
