# Kruskal's algo to find minimum spanning tree
# of a given connected, undirected and weighted graph.

from collections import defaultdict

class Graph:
	def __init__(self, vertices):
		self.v = vertices
		self.graph = []

	def addEdge(self, u, v, w):
		self.graph.append([u, v, w])

	# An util method to find set of an element i
	# (uses path compression technique)
	def find(self, parent, i):
		if parent[i] == i:
			return i
		else:
			parent[i] = self.find(parent, parent[i])
			return parent[i]

	# A function that does union of two sets of x and y
	# (uses union by rank)
	def union(self,parent, rank, x, y):
		xroot = self.find(parent, x)
		yroot = self.find(parent, y)

		if rank[xroot] < rank[yroot]:
			parent[xroot] = yroot
		elif rank[xroot] > rank[yroot]:
			parent[yroot] = xroot
		else:
			parent[yroot] = xroot
			rank[xroot] += 1

	def KruskalMST(self):
		result = []
		i = 0
		e = 0

		self.graph = sorted(self.graph, key=lambda item: item[2])
		parent = [] ; rank = []

		# Create v subsets with single elements
		for node in range(self.v):
			parent.append(node)
			rank.append(0)

		# Number of edges to be taken is equal to v-1
		while e < self.v - 1:
			u, v, w = self.graph[i]
			i += 1
			x = self.find(parent, u)
			y = self.find(parent, v)

			if x != y:
				e += 1
				result.append([u, v, w])
				self.union(parent, rank, x, y)

		# print "PARENT:", parent
		# print "RANK:", rank
		# print "RESULT:", result
		print "Following are the edges in the constructed MST"
		for u, v, w in result:
			print "{}...{}->{}".format(u, v, w)


if __name__ == '__main__':
	g = Graph(4)
	g.addEdge(0, 1, 10)
	g.addEdge(0, 2, 6)
	g.addEdge(0, 3, 5)
	g.addEdge(1, 3, 15)
	g.addEdge(2, 3, 4)
	
	g.KruskalMST()
