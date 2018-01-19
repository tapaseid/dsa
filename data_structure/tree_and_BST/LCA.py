# Lowest common ancestor for binary tree
# Different from BST

import pickle

class Node:
	def __init__(self, data=None):
		self.left = None
		self.right = None
		self.data = data

def findPath(root, p, n):
	# Util method for LCA()

	if root is None:
		return False
	
	p.append(root.data)

	if root.data == n:
		return True

	if ((root.left is not None and findPath(root.left, p, n)) or
			(root.right is not None and findPath(root.right, p, n))):
		return True

	p.pop()
	return False 

def LCA(root, n1, n2):
	# Time complexity O(n)

	if root is None:
		return
	path1 = []
	path2 = []

	if not findPath(root, path1, n1) or not findPath(root, path2, n2):
		return -1

	# print path1, path2
	i = 0
	while i < len(path1) and i < len(path2):
		if path1[i] != path2[i]:
			break
		i += 1

	return path1[i-1]


def findLCA(root, n1, n2):
	# Time complexity O(n)
	# Both nodes should present, otherwise return the existing node!
	# So, this is not complete solution!!!!! look for findLCA_another()

	if root is None:
		return

	if root.data == n1 or root.data == n2:
		return root.data

	left_lca = findLCA(root.left, n1, n2)
	right_lca = findLCA(root.right, n1, n2)

	if left_lca and right_lca:
		return root.data

	return left_lca if left_lca is not None else right_lca

def findLCA_another(root, n1, n2):
	# This is the complete solution of findLCA()

	v = [False, False]
	lca = findLCAUtil(root, n1, n2, v)

	if (v[0] and v[1] or v[0] and find(lca, n2) or v[1] and find(lca, n1)):
		return lca.data
	return None

def find(root, n):
	if root is None:
		return False

	if root.data == n or find(root.left, n) or find(root.right, n):
		return True
	return False

def findLCAUtil(root, n1, n2, v):
	if root is None:
		return None

	if root.data == n1:
		v[0] = True
		return root
	if root.data == n2:
		v[1] = True
		return root

	left_lca = findLCAUtil(root.left, n1, n2, v)
	right_lca = findLCAUtil(root.right, n1, n2, v)

	if left_lca and right_lca:
		return root
	return left_lca if left_lca is not None else right_lca


if __name__ == '__main__':
	with open("util/file", "r") as f:
		root = pickle.load(f)

	print findLCA_another(root, 4, 2)
