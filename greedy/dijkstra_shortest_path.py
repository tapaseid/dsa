# Dijkstar's algo to find a shortest path of a given
# connected, undirected and weighted graph
import sys

class Graph:
	def __init__(self, vertices):
		self.v = vertices
		self.graph = [[0 for i in range(self.v)] for j in range(self.v)]

	def minDistance(self, dist, sptSet):
		minimum = sys.maxint
		for node in range(self.v):
			if minimum > dist[node] and sptSet[node] == False:
				minimum = dist[node]
				min_index = node
		return min_index

	def printSPT(self, parent):
		print "Edge \tWeight"
		for i in range(1, self.v):
			print parent[i], "-", i, "\t", self.graph[i][parent[i]]

	def printSolution(self, dist):
		print "Vertex \tDistance from source"
		for node in range(self.v):
			print node, "\t", dist[node]

	def dijkstraSPT(self, start):
		dist = [sys.maxint]*self.v
		dist[start] = 0
		sptSet = [False]*self.v
		parent = [None]*self.v
		parent[start] = -1

		for count in range(self.v):

			u = self.minDistance(dist, sptSet)
			sptSet[u] = True

			for v in range(self.v):
				if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
					dist[v] = dist[u] + self.graph[u][v]
					parent[v] = u

		self.printSPT(parent)
		self.printSolution(dist)


if __name__ == '__main__':
	g = Graph(9)
	g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
			   [4, 0, 8, 0, 0, 0, 0, 11, 0],
			   [0, 8, 0, 7, 0, 4, 0, 0, 2],
			   [0, 0, 7, 0, 9, 14, 0, 0, 0],
			   [0, 0, 0, 9, 0, 10, 0, 0, 0],
			   [0, 0, 4, 14, 10, 0, 2, 0, 0],
			   [0, 0, 0, 0, 0, 2, 0, 1, 6],
			   [8, 11, 0, 0, 0, 0, 1, 0, 7],
			   [0, 0, 2, 0, 0, 0, 6, 7, 0]
			  ]
	g.dijkstraSPT(0)
