#bubble sort

def bubbleSort(arr):
	n = len(arr)
	swap = False
	for i in range(n-1):
		swap = False
		for j in range(n-1-i):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swap = True
		if not swap:
			break
	return arr

# driver method
if __name__ == '__main__':
	arr = [8, 2, 4, 9, 3, 6]
	print bubbleSort(arr)
