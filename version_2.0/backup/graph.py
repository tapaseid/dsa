
### Leetcode - 547. Number of Provinces
### https://www.youtube.com/watch?v=8f1XPm4WOUc&ab_channel=NeetCode

# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        # Use a rank array to record the height of each vertex, i.e., the "rank" of each vertex.
        # The initial "rank" of each vertex is 1, because each of them is
        # a standalone vertex with no connection to other vertices.
        self.rank = [1] * size
        self.count = size

    # The find function here is the same as that in the disjoint set with path compression.
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # The union function with union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            self.count -= 1

    def getCount(self):
        return self.count


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected or len(isConnected) == 0:
            return 0
        n = len(isConnected)
        uf = UnionFind(n)
        for row in range(n):
            for col in range(row + 1, n):
                if isConnected[row][col] == 1:
                    uf.union(row, col)
        return uf.getCount()

#--------------------------------------------------------------------
def findCircleNum(isConnected):
    """
    :type isConnected: List[List[int]]
    :rtype: int
    """
#         def dfs(i):
#             visited[i] = True
#             for nei, adj in enumerate(isConnected[i]):
#                 if adj and not visited[nei]:
#                     dfs(nei)
    
#         n = len(isConnected)
#         count = 0
#         visited = [False]*n
#         for i in range(n):
#             if not visited[i]:
#                 dfs(i)
#                 count += 1
#         return count

    def find(x):
        if x == root[x]:
            return x
        root[x] = find(root[x])
        return root[x]
    
    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            if rank[rootX] > rank[rootY]:
                root[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                root[rootX] = rootY
            else:
                root[rootY] = rootX
                rank[rootX] += 1
            return 1
        return 0
    
    root = [i for i in range(len(isConnected))]
    rank = [1]*(len(isConnected))
    
    count = len(isConnected)
    for i in range(len(isConnected)):
        for j, adj in enumerate(isConnected[i]):
            if adj:
                count -= union(i, j)
    return count

# isConnected = [[1,1,0],[1,1,0],[0,0,1]]
isConnected = [[1,0,0],[0,1,0],[0,0,1]]

# print findCircleNum(isConnected)


######################################################################

from collections import defaultdict
class Graph:
	def __init__(self, size=None):
		self.graph = defaultdict(list)
		self.size = size

	def add(self, u, v):
		self.graph[u].append(v)
		# self.graph[v].append(u)

	@property
	def print_graph(self):
		for key in self.graph:
			print "{}: {}".format(key, self.graph[key])

	def detect_cycle_in_undirected_graph(self):
		visited = [False]*self.size

		for vertex in range(self.size):
			if not visited[vertex]:
				if self.dfs_for_undirected_graph(vertex, visited, -1):
					return True
		return False

	def dfs_for_undirected_graph(self, vertex, visited, parent):
		visited[vertex] = True
		for i in self.graph[vertex]:
			if not visited[i]:
				if self.dfs_for_undirected_graph(i, visited, vertex):
					return True
			elif parent != i:
				return True
		return False

	def detect_cycle_in_directed_graph(self):
		visited = [False]*self.size
		rec_stack = [False]*self.size

		for vertex in range(self.size):
			if not visited[vertex]:
				if self.dfs_for_directed_graph(vertex, visited, rec_stack):
					return True
		return False

	def dfs_for_directed_graph(self, vertex, visited, rec_stack):
		visited[vertex] = True
		rec_stack[vertex] = True
		for neighbour in self.graph[vertex]:
			if not visited[neighbour]:
				if self.dfs_for_directed_graph(neighbour, visited, rec_stack):
					return True
			elif rec_stack[neighbour]:
				return True

		rec_stack[vertex] = False
		return False

	def is_reachable(self, src, dest):
		visited = [False]*self.size

		q = []
		q.append(src)
		visited[src] = True

		while q:
			tmp = q.pop(0)

			if tmp == dest:
				return True

			for i in self.graph[tmp]:
				if not visited[i]:
					visited[i] = True
					q.append(i)

		return False

if __name__ == '__main__':
	size = 8
	obj = Graph(size)

	obj.add(0, 1)
	obj.add(2, 0)
	obj.add(1, 3)
	obj.add(1, 2)
	obj.add(4, 3)
	obj.add(4, 5)
	obj.add(6, 7)
	# obj.print_graph
	# print obj.detect_cycle_in_undirected_graph()
	# print obj.detect_cycle_in_directed_graph()


	# Given a directed/undirected graph, design an algorithm to find out whether there is a route between two nodes.
	print obj.is_reachable(0, 5)
	# Try to find minimum path sum also between two nodes.

