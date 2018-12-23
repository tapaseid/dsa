class Node:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.prev = None
		self.next = None

class LRU:
	def __init__(self, capacity):
		self.capacity = capacity
		self.dict = dict()
		self.head = Node(0, 0)
		self.tail = Node(0, 0)
		self.head.next = self.tail
		self.tail.prev = self.head

	def _remove(self, node):
		prev = node.prev
		nxt = node.next
		prev.next = nxt
		nxt.prev = prev

	def _add(self, node):
		prev = self.tail.prev
		prev.next = node
		node.prev = prev
		node.next = self.tail
		self.tail.prev = node

	def get(self, key):
		if key in self.dict:
			node = self.dict[key]
			self._remove(node)
			self._add(node)
			return node.value
		return -1	

	def put(self, key, value):
		if key in self.dict:
			self._remove(self.dict[key])
		node = Node(key, value)
		self._add(node)
		self.dict[key] = node
		if len(self.dict) > self.capacity:
			node = self.head.next
			self._remove(node)
			del self.dict[node.key]






