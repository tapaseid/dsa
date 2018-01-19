# Binary tree

import os, sys
import pickle

class Node:
	def __init__(self, data=None):
		self.left = None
		self.right = None
		self.data = data

class BinaryTree:

	def inorder(self, root):
		if root:
			self.inorder(root.left)
			print root.data,
			self.inorder(root.right)

	def printLevelOrder(self, root):
		h = self.height(root)
		for i in range(1, h+1):
			self.printGivenLevel(root, i)

	def printGivenLevel(self, root, level):
		if root is None:
			return
		if level==1:
			print root.data,
		self.printGivenLevel(root.left, level-1)
		self.printGivenLevel(root.right, level-1)
		

	def height(self, root):
		if root is None:
			return 0
		# if root.left is None:
		# 	return 1 + self.height(root.right)
		# elif root.right is None:
		# 	return 1 + self.height(root.left)
		# else:
		return 1 + max(self.height(root.left), self.height(root.right))

	def printLevelOrder_Queue(self, root):
		if root is None:
			return
		q = []
		q.append(root)
		while len(q):
			print q[0].data,
			node = q.pop(0)
			if node.left:
				q.append(node.left)
			if node.right:
				q.append(node.right)

	def diameter(self, root):
		if root is None:
			return

		return max(self.height(root.left) + 1 + self.height(root.right),
			max(self.diameter(root.left), self.diameter(root.right)))

	def height_diameter(self, node):
		if node is None:
			return 0, 0
		ld, lh = self.height_diameter(node.left)
		rd, rh = self.height_diameter(node.right)
		return max(ld, rd, lh + rh +1), 1 + max(lh, rh)


	def diameterOpt(self, root):
		d, _ = self.height_diameter(root)
		return d

	def inorderStack(self, root):
		current = root
		s = []
		done = 0
		while(not done):
			if current is not None:
				s.append(current)
				current = current.left
			else:
				if(len(s)):
					current = s.pop()
					print current.data,
					current = current.right
				else:
					done = 1

	def inOrderMorrisTraversal(self, root):
		current = root
		while current is not None:
			if current.left is None:
				print current.data,
				current = current.right
			else:
				pre = current.left
				while(pre.right is not None and pre.right != current):
					pre = pre.right
				if pre.right is None:
					pre.right = current
					current = current.left
				else:
					pre.right = None
					print current.data,
					current = current.right

if __name__ == '__main__':
	binary_tree = BinaryTree()
	with open("util/file", 'r') as f:
		r = pickle.load(f)

	binary_tree.inorder(r)
	print
	binary_tree.printLevelOrder(r)
	print
	binary_tree.printLevelOrder_Queue(r)
	print
	print binary_tree.height(r)
	print binary_tree.diameter(r)
	print binary_tree.diameterOpt(r)
	binary_tree.inorderStack(r)
	print
	binary_tree.inOrderMorrisTraversal(r)
