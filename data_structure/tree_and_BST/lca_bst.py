# Lowest common ancestor for BST

class NodeBST:
	def __init__(self, data=None):
		self.data = data
		self.left = None
		self.right = None

def lca(root, n1, n2):
	if root is None:
		return
	if root.data > n1 and root.data > n2:
		return lca(root.left, n1, n2)
	if root.data < n1 and root.data < n2:
		return lca(root.right, n1, n2)
	return root.data

if __name__ == '__main__':
	root = NodeBST(20)
	root.left = NodeBST(10)
	root.left.left = NodeBST(5)
	root.left.right = NodeBST(15)
	root.right = NodeBST(30)
	root.right.left = NodeBST(25)
	root.right.right = NodeBST(35)

	print lca(root, 5, 25)
