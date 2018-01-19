# heap sort

def heapify(arr, n, i):
	largest = i #initialize largest as root
	l = 2*i + 1 #left = 2*i +1
	r = 2*i +2  #right = 2*i +2

	#see if left chile of root exists and is greater than root
	if l < n and arr[i] < arr[l]:
		largest = l

	#see if right child of root exists and is greater than root
	if r < n and arr[largest] < arr[r]:
		largest = r
	
	#change the root if needed
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i] #swap

		#heapify the root
		heapify(arr, n, largest)


def heapSort(arr):
	n = len(arr)

	if n > 1:
		#build a max-heap
		for i in range(n/2, -1, -1):
			heapify(arr, n, i)

		#one by one extract elements
		for i in range(n-1, 0, -1):
			arr[i], arr[0] = arr[0], arr[i] #swap
			heapify(arr, i, 0)

	return arr

# driver method
if __name__ == '__main__':
	arr = [8, 2, 4, 9, 3, 6]
	print heapSort(arr)




#Application
# k largest elements form an array(unsorted)
def k_largest_elements(a_unsort, k):
	n = len(a_unsort)
	for i in range(n/2, -1, -1):
		heapify(a_unsort, n, i)
	
	index = n-1
	for i in range(k):
		a_unsort[index], a_unsort[0] = a_unsort[0], a_unsort[index]
		print a_unsort[index]
		heapify(a_unsort, index, 0)
		index -= 1

def kth_largest(a_unsort, k):
	n = len(a_unsort)
	for i in range(n/2, -1, -1):
		heapify(a_unsort, n, i)
	
	index = n-1
	for i in range(k):
		a_unsort[index], a_unsort[0] = a_unsort[0], a_unsort[index]
		heapify(a_unsort, index, 0)
		index -= 1
	return a_unsort[index+1]

if __name__ == '__main__':
	a_unsort = [1, 23, 12, 9, 30, 2, 50]

	# k_largest_elements(a_unsort, 3)

	print kth_largest(a_unsort, 2)
