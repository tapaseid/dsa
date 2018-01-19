# To demonstrate min heap and it's operations
from heapq import heappush, heappop, heapify

class MinHeap:
	def __init__(self):
		self.heap = []

	def getMin(self):
		if len(self.heap):
			return self.heap[0]
		return "heap is empty"

	def extractMin(self):
		self.heap.pop(0)
		heapify(self.heap)

	def decreaseKey(self, index, value):
		self.heap[index] -= value
		heapify(self.heap)

	def insert(self, key):
		self.heap.append(key)
		heapify(self.heap)

	def delete(self, index):
		self.decreaseKey(index, 1000)
		self.extractMin()

# arr = [4, 10, 3, 5, 1]
# heapify(arr)
# print arr


if __name__ == '__main__':
	h = MinHeap()
	h.insert(4)
	h.insert(10)
	h.insert(3)
	h.insert(5)
	h.insert(1)
	print h.heap
	
	print h.getMin()
	
	h.extractMin()
	print h.heap
	
	h.decreaseKey(2, 3)
	print h.heap

	h.delete(3)
	print h.heap
