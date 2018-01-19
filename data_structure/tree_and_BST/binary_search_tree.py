# Binary search tree

class Node:
	def __init__(self, data=None):
		self.data = data
		self.left = None
		self.right = None

class BST:
	def search(self, root, key):
		if root is None or root.data == key:
			return root

		if root.data < key:
			return self.search(root.right, key)
		else:
			return self.search(root.left, key)

	def insert(self, root, key):
		if root is None:
			return Node(key)

		if root.data < key:
			if root.right is None:
				root.right = Node(key)
			else:
				root.right = self.insert(root.right, key)
		else:
			if root.left is None:
				root.left = Node(key)
			else:
				root.left = self.insert(root.left, key)

		return root

	def delete(self, root, key):
		if root is None:
			return

		if root.data > key:
			root.left = self.delete(root.left, key)
		elif root.data < key:
			root.right = self.delete(root.right, key)

		else:
			if root.left is None:
				temp = root.right
				root = None
				return temp
			if root.right is None:
				temp = root.left
				root = None
				return temp

			temp = self.minValueNode(root.right)
			root.data = temp.data
			root.right = self.delete(root.right, temp.data)

		return root


	def minValueNode(self, root):
		current = root

		while current.left is not None:
			current = current.left
		return current

	def inOrede(self, root):
		if root is not None:
			self.inOrede(root.left)
			print root.data,
			self.inOrede(root.right)


if __name__ == '__main__':
	arr = [50, 30, 70, 20, 40, 60, 80]
	bst = BST()
	root = None
	for i in arr:
		root = bst.insert(root, i)
	
	bst.inOrede(root)
	print

	if bst.search(root, 60): print "Found", bst.search(root, 60).data
	else: print "Not found"

	print "inserting....90"
	bst.insert(root, 90)
	bst.inOrede(root)
	print

	print "deleting..."
	root = bst.delete(root, 50)
	# print root.data
	bst.inOrede(root)
