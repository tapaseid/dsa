
# Given a binary tree with unique integer values. Return the vector of 
# roots of subtrees formed after removing the given node.

class BTNode:
	def __init__(self, id=None):
		self.id = id
		self.left = None
		self.right = None

def removeNode(root, nodeToBeRemoved):
	res = []

	if root.id == nodeToBeRemoved:
		if root.left:
			res.append(root.left.id)
		if root.right:
			res.append(root.right.id)
	else:
		res.append(root.id)
		def helper(root):
			if root is None:
				return

			if root.id == nodeToBeRemoved:
				if root.left:
					res.append(root.left.id)
				if root.right:
					res.append(root.right.id)
				return
			helper(root.left)
			helper(root.right)
		helper(root)

	return res

def removeNode2(root, nodeToBeRemoved):
	ans = []

	def dfs(root):
		if not root:
			return None

		root.left = dfs(root.left)
		root.right = dfs(root.right)

		if root.id == nodeToBeRemoved:
			if root.left:
				ans.append(root.left.id)
			if root.right:
				ans.append(root.right.id)
			return None

		return root

	dfs(root)
	if root.id != nodeToBeRemoved:
		ans.insert(0, root.id)

	return ans

def removeNode_iterative(root, nodeToBeRemoved):
	q = [[root, False]]
	res = []
	while q:
		node, has_parent = q.pop(0)

		if not has_parent and node.id != nodeToBeRemoved:
			res.append(node.id)

		has_parent = False if node.id == nodeToBeRemoved else True

		if node.left:
			q.append([node.left, has_parent])

		if node.right:
			q.append([node.right, has_parent])

	return res

def main(root):
	for i in range(len(TEST_INPUT)):
		print "Running test case {}:...".format(i+1)

		# print removeNode(root, TEST_INPUT[i])
		# assert TEST_OUTPUT[i] == removeNode(root, TEST_INPUT[i]), "Wrong answer!"

		# print removeNode2(root, TEST_INPUT[i])
		# assert TEST_OUTPUT[i] == removeNode2(root, TEST_INPUT[i]), "Wrong answer!"

		# print removeNode_iterative(root, TEST_INPUT[i])
		assert TEST_OUTPUT[i] == removeNode_iterative(root, TEST_INPUT[i]), "Wrong answer!"
	print "All test cases passed!"


def number_of_del(input_sring):
    res = 0
    
    i = 0
    while i < len(input_sring) - 1:
        tmp_count = 0
        while i < len(input_sring) - 1 and input_sring[i+1] == input_sring[i]:
            tmp_count += 1
            i += 1
        res += tmp_count
        i += 1
        
    return res

if __name__ == '__main__':
	root = BTNode(1)
	root.left = BTNode(2)
	root.right = BTNode(3)
	root.left.left = BTNode(4)
	root.left.right = BTNode(5)
	root.right.left = BTNode(6)
	root.right.left.left = BTNode(7)

	TEST_INPUT = [
				  1,
				  2
				 ]
	TEST_OUTPUT = [
					[2, 3],
					[1, 4, 5]
				  ]

	# main(root)

	s = 'ababab'
	print number_of_del(s)











