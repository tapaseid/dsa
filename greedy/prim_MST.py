# Prim's algo to to find minimum spanning tree
# of a given connected, undirected and weighted graph.

import sys

class Graph:
	def __init__(self, vertices):
		self.v = vertices
		self.graph = [[0 for col in range(vertices)] for row in range(vertices)]

	# A utility function to print the constructed MST stored in parent[]
	def printMST(self, parent):
		print "Edge \tWeight"
		for i in range(1, self.v):
			print parent[i], "-", i, "\t", self.graph[i][parent[i]]

	# A utility function to find the vertex with minimum distance value, from
    # the set of vertices not yet included in shortest path tree
	def minKey(self, key, mstSet):
		minimum = sys.maxint
		for v in range(self.v):
			if key[v] < minimum and mstSet[v] == False:
				minimum = key[v]
				min_index = v
		return min_index

	def PrimMST(self):
		key = [sys.maxint]*self.v
		parent = [None]*self.v  # Array to store constructed MST
		key[0] = 0  # Make key 0 so that this vertex is picked as first vertex
		mstSet = [False]*self.v
		parent[0] = -1  # First node is always the root

		for cout in range(self.v):

			# Pick the minimum distance vertex from the set of vertices not
			# yet processed. u is always equal to src in first iteration
			u = self.minKey(key, mstSet)

			# Put the minimum distance vertex in the shortest path tree
			mstSet[u] = True


			for v in range(self.v):
				# update key[] to pick min in next iteration
				if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
					key[v] = self.graph[u][v]
					parent[v] = u  # set parent node to keep track

		self.printMST(parent)

if __name__ == '__main__':
	g = Graph(5)
	g.graph = [[0, 2, 0, 6, 0],
			   [2, 0, 3, 8, 5],
			   [0, 3, 0, 0, 7],
			   [6, 8, 0, 0, 9],
			   [0, 5, 7, 9, 0]
			  ]

	g.PrimMST()
