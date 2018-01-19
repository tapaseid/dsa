# B-Tree: Extension of BST(B-tree of order 2). order => 2*degree -1

# Properties of B-Tree
# --------------------
# 1) All leaves are at same level.
# 2) A B-Tree is defined by the term minimum degree t.
#	 The value of t depends upon disk block size.
# 3) Every node except root must contain at least t-1 keys.
#	 Root may contain minimum 1 key.
# 4) All nodes(including root) may contain at most 2t-1 keys.
# 5) Number of children of a node is equal to the number of keys in it plus 1.
# 6) All keys of a node are sorted in increasing order.
#	 The child between two keys k1 and k2 contains all keys in range from k1 and k2.
# 7) B-Tree grows and shrinks from root which is unlike Binary Search Tree.
#	 Binary Search Trees grow downward and also shrink from downward.
# 8) Like other balanced Binary Search Trees, time complexity to search, insert and delete is O(Logn).


class BTreeNode:
	def __init__(self, leaf=False):
		self.isLeaf = leaf
		self.keys = []
		self.c = []

class B_Tree:
	def __init__(self, degree):
		self.root = BTreeNode(leaf=True)
		self.degree = degree
		if self.degree <= 1:
			raise ValueError("B-Tree must have a degree of 2 or more!")

	def insert(self, pos, key):
		r = self.root
		if len(r.keys) == (2*self.degree) - 1: # keys are full, we must split
			s = BTreeNode()
			self.root = s
			s.c.insert(0, r)    # former root is now 0th child of new root s
			self._split_Child(s, 0)
			self._insert_NonFull(s, key)

		else:
			self._insert_NonFull(r, key)

	def _insert_NonFull(self, r, k):
		i = len(r.keys)-1
		if r.isLeaf:
			# insert a key
			r.keys.append(0)
			while i >= 0 and k < r.keys[i]:
				r.keys[i+1] = r.keys[i]
				i -= 1
			r.keys[i+1] = k

		else:
			# insert a child
			while i >= 0 and k < r.keys[i]:
				i -= 1
			i += 1
			if len(r.c[i].keys) == (2*self.degree) - 1:
				self._split_Child(r, i)
				if k > r.keys[i]:
					i += 1

			self._insert_NonFull(r.c[i], k)

	def _split_Child(self, r, pos):
		d = self.degree
		y = r.c[pos]
		z = BTreeNode(leaf=y.isLeaf)

		# slide all children of r to the right and insert z at pos+1
		r.c.insert(pos+1, z)
		r.keys.insert(i, y.keys[d-1])

		# keys if z are d to 2d-1,
		# y is then 0 to d-2
		z.keys = y.keys[d:(2*d - 1)]
		y.keys = y.keys[0:(d-1)]

		if not y.isLeaf:
			z.c = y.c[d:(2*d)]
			y.c = y.c[0:(d-1)]

	def delete(self, key):
		pass

	def search(self, key, node=None): 
		if node is None:
			node = self.root

		if key in node.keys:
			return True
		elif node.isLeaf:
			return False
		else:
			i = 0
			while i < len(node.keys) and key > node.keys[i]:
				i += 1
			return self.search(key, node.c[i])

	def level_order_print(self):
		this_level = [self.root]
		while this_level:
			next_level = []
			output = ""
			for node in this_level:
				if node.c:
					next_level.extend(node.c)
				output += str(node.keys) + " "
			print output
			this_level = next_level


if __name__ == '__main__':
	arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
	b_tree = B_Tree(2)

	for i in arr:
		b_tree.insert(0, i)
		# b_tree.level_order_print()
		# print "....."

	b_tree.level_order_print()

	if b_tree.search(80): print "Found!"
	else: print "Not found!"
