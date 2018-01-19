# This module will check if a graph has cycle or not.

from collections import defaultdict

def MakeSet(x)
	x.parent = x
	x.rank = 0

def Find(x):
	if x.parent == x:
		return x
	else:
		x.parent = Find(x.parent)
		return x.parent

def Union(x, y):
	xRoot = Find(x)
	yRoot = Find(y)
	if xRoot == yRoot:
		return
	if xRoot.rank < yRoot.rank:
		xRoot.parent = yRoot
	elif xRoot.rank > yRoot.rank:
		yRoot.parent = xRoot
	else:
		xRoot.parent = yRoot
		yRoot.rank += 1



class Graph:
	def __init__(self, vertices):
		self.graph = defaultdict(list)
		self.v = vertices

	def addEdge(self, u, v):
		self.graph[u].append(v)

	

	#For directed graph
	def detect_cycle_for_directed(self):
		visited = [False]*self.v
		recStack = [False]*self.v
		for node in range(self.v):
			if visited[node] == False:
				if self.isCycleUtil_for_directed(node, visited, recStack) == True:
					return True
		return False

	def isCycleUtil_for_directed(self, node, visited, recStack):
		visited[node] = True
		recStack[node] = True
		for neighbours in self.graph[node]:
			if visited[neighbours] == False:
				if self.isCycleUtil_for_directed(neighbours, visited, recStack) == True:
					return True
			elif recStack[neighbours] == True:
				return True
		
		recStack[node] = False
		return False

	
	
	# # For undirected graph
	# def detect_cycle_for_undirected(self):
	# 	parent = [-1]*self.v
	# 	for i in self.graph:
	# 		for j in self.graph[i]:
	# 			x = self.find_parent(parent, i)
	# 			y = self.find_parent(parent, j)
	# 			if x == y:
	# 				return True
	# 			self.union(parent, x, y)

	# def find_parent(self, parent, node):
	# 	if parent[node] == -1:
	# 		return node
	# 	else:
	# 		return self.find_parent(parent, parent[node])

	# def union(self, parent, x, y):
	# 	x_set = self.find_parent(parent, x)
	# 	y_set = self.find_parent(parent, y)
	# 	parent[x_set] = y_set

	#(Better method because of union by rank and path compression)
	def detect_cycle_for_undirected(self):
		parent = [i for i in range(self.v)]
		rank = [0 for i in range(self.v)]
		for i in self.graph:
			for j in self.graph[i]:
				x = self.Find(parent, i)
				y = self.Find(parent, j)
				if x == y:
					return True
				self.Union(parent, rank, x, y)
			# print "{} union:{}, rank:{}".format(i, parent, rank)


	def Find(self, parent, x):
		if parent[x] == x:
			return x
		else:
			parent[x] = self.Find(parent, parent[x])
			return parent[x]

	def Union(self, parent, rank, x, y):
		xRoot = self.Find(parent, x)
		yRoot = self.Find(parent, y)
		if xRoot == yRoot:
			return
		if rank[xRoot] < rank[yRoot]:
			parent[xRoot] = yRoot
		elif rank[xRoot] > rank[yRoot]:
			parent[yRoot] = xRoot
		else:
			parent[xRoot] = yRoot
			rank[yRoot] += 1


if __name__ == '__main__':
	
	#directed graph
	g = Graph(4)
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(1, 2)
	g.addEdge(2, 0)
	g.addEdge(2, 3)
	g.addEdge(3, 3)
	
	if g.detect_cycle_for_directed():
		print "Found!"
	else:
		print "Not found!"


	#undirected graph
	g = Graph(3)
	g.addEdge(0, 1)
	g.addEdge(1, 2)
	# g.addEdge(2, 0)
	g.addEdge(0,2)
	 
	if g.detect_cycle_for_undirected():
	    print "Graph contains cycle"
	else :
	    print "Graph does not contain cycle "
