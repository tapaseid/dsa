# Topological sort

from collections import defaultdict

class Topological_sort:
	def __init__(self, size=None):
		self.graph = defaultdict(list)
		self.size = size

	def add(self, u, v):
		self.graph[u].append(v)

	@property
	def topological(self):
		n = len(self.graph)
		visited = [False]*self.size
		stack = []

		for i in range(self.size):
			if not visited[i]:
				self._helper(visited, stack, i)
		print stack

	def _helper(self, visited, stack, v):
		visited[v] = True
		for i in self.graph[v]:
			if not visited[i]:
				self._helper(visited, stack, i)
		stack.insert(0, v)


if __name__ == '__main__':
	obj = Topological_sort(6)
	obj.add(5, 0)
	obj.add(4, 0)
	obj.add(5, 2)
	obj.add(4, 1)
	obj.add(2, 3)
	obj.add(3, 1)
	obj.topological

