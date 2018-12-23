class Node:
	def __init__(self, data=None):
		self.data = data
		self.right = None
		self.down = None

def push(root, val):
	new_node = Node(val)
	new_node.down = root
	root = new_node

	return root

def merge(a, b):
	if a is None:
		return b
	if b is None:
		return a
	result = Node()
	if a.data<b.data:
		result = a
		result.down = merge(a.down, b)
	else:
		result = b
		result.down = merge(a, b.down)
	return result

def flatten(root):
	if root is None or root.right is None:
		return root

	return merge(root, flatten(root.right))

def print_list(root):
	while root is not None:
		print root.data
		root = root.down

if __name__ == '__main__':
	root = None
	root = push(root, 30)
	root = push(root, 8)
	root = push(root, 7)
	root = push(root, 5)
	root.right = push(root.right, 20)
	root.right = push(root.right, 10)
	root.right.right = push(root.right.right, 50)
	root.right.right = push(root.right.right, 22)
	root.right.right = push(root.right.right, 19)
	root.right.right.right = push(root.right.right.right, 45)
	root.right.right.right = push(root.right.right.right, 40)
	root.right.right.right = push(root.right.right.right, 35)
	root.right.right.right = push(root.right.right.right, 28)

	root = flatten(root)
	print_list(root)
