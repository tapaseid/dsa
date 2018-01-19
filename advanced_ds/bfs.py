# breath first traversal for graph

from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def BFS(self, v):
		visited = [False]*(len(self.graph))

		queue = []

		queue.append(v)
		visited[v] = True

		while queue:
			val = queue.pop(0)
			print val,

			for i in self.graph[val]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True

if __name__ == '__main__':
	g = Graph()
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(1, 2)
	g.addEdge(2, 0)
	g.addEdge(2, 3)
	g.addEdge(3, 3)
	g.BFS(2)

