# depth first traversal for graph

from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self, u, v):
		self.graph[u].append(v)

	@property
	def dfs(self):
		# print self.graph
		visited = [False]*(len(self.graph))

		# for connected graph
		# self.dfsUtil(visited, 2)

		# for disconnected graph
		for v in self.graph:
			if visited[v] == False:
				self.dfsUtil(visited, v)

	def dfsUtil(self, visited, v):
		visited[v] = True
		print v,
		for i in self.graph[v]:
			if visited[i] == False:
				self.dfsUtil(visited, i)

if __name__ == '__main__':
	g = Graph()
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(1, 2)
	g.addEdge(2, 0)
	g.addEdge(2, 3)
	g.addEdge(3, 3)
	g.addEdge(4, 5)
	g.addEdge(4, 6)
	g.addEdge(5, 6)
	g.addEdge(6, 5)
	g.dfs
