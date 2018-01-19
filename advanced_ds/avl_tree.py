# AVL tree topics.

class TreeNode:
	def __init__(self, data=None):
		self.data = data
		self.left = None
		self.right = None
		self.height = 1
		self.count = 1

class AVL:
	def insert(self, root, key):

		if root is None:
			return TreeNode(key)

		# for duplicate nodes!
		if key == root.data:
			root.count += 1
			return root

		elif key < root.data:
			root.left = self.insert(root.left, key)
		else:
			root.right = self.insert(root.right, key)

		root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
		balance = self.getBalance(root)
		# print "balance: {}, left: {}, right: {}".format(balance, root.left, root.right)
		
		# LL
		if balance>1 and key<root.left.data:
			return self.rightRotate(root)

		# LR
		if balance>1 and key>root.left.data:
			root.left = self.leftRotate(root.left)
			return self.rightRotate(root)

		# RR
		if balance<-1 and key>root.right.data:
			return self.leftRotate(root)

		# RL
		if balance<-1 and key<root.right.data:
			root.right = self.rightRotate(root.right)
			return self.leftRotate(root)

		return root

	def delete(self, root, key):
		if root is None:
			return root

		elif key < root.data:
			root.left = self.delete(root.left, key)
		elif key > root.data:
			root.right = self.delete(root.right,key)
		
		else:

			# for duplicate nodes!
			if root.count > 1:
				root.count -= 1
				return root

			if root.left is None:
				temp = root.right
				root = None
				return temp
			if root.right is None:
				temp = root.left
				root = None
				return temp
			temp = self.getMinValueNode(root.right)
			root.data = temp.data
			root.right = self.delete(root.right, temp.data)

		if root is None:
			return root

		root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
		balance = self.getBalance(root)

		# LL
		if balance > 1 and self.getBalance(root.left) >= 0:
			return self.rightRotate(root)
		
		# LR
		if balance > 1 and self.getBalance(root) < 0:
			root.left = self.leftRotate(root.left)
			return self.rightRotate(root)

		# RR
		if balance < -1 and self.getBalance(root.right) <= 0:
			return self.leftRotate(root)

		# RL
		if balance < -1 and self.getBalance(root.right) > 0:
			root.right = self.rightRotate(root.right)
			return self.leftRotate(root)

		return root


	def search(self, root, key):
		if root is None:
			return 0

		if root.data == key:
			return 1
		elif key < root.data:
			return self.search(root.left, key)
		else:
			return self.search(root.right, key)

	def leftRotate(self, x):
		y = x.right
		T2 = y.left

		y.left = x
		x.right = T2
		x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
		y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

		return y

	def rightRotate(self, x):
		y = x.left
		T3 = y.right

		y.right = x
		x.left = T3
		x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
		y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

		return y

	def getHeight(self, root):
		if root is None:
			return 0
		return root.height

		# return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

	def getBalance(self, root):
		if root is None:
			return 0

		return self.getHeight(root.left)-self.getHeight(root.right)

	def getMinValueNode(self, root):
		if root is None or root.left is None:
			return root
		return self.getMinValueNode(root.left)

	def preOrder(self, root):
		if root is None:
			return

		print "{}({})".format(root.data, root.count),
		self.preOrder(root.left)
		self.preOrder(root.right)

 
if __name__ == '__main__':
	avl_tree = AVL()
	root = None
	arr = [10, 20, 30, 40, 50, 25, 20, 50, 10]
	for i in arr:
		# print "Inserting {}".format(i)
		root = avl_tree.insert(root, i)
		# print "... {} is inserted".format(i)

	avl_tree.preOrder(root)

	if avl_tree.search(root, 10): print "\nFound!"
	else: print "\nNot found!"

	avl_tree.delete(root, 10)
	avl_tree.preOrder(root)
