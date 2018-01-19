# selection sort

def selectionSort(arr):
	n = len(arr)
	for i in range(n-1):
		min_indx = i
		for j in range(i+1, n):
			if arr[j] < arr[min_indx]:
				min_indx = j
		arr[i], arr[min_indx] = arr[min_indx], arr[i]
	return arr


# driver method
if __name__ == '__main__':
	arr = [8, 2, 4, 9, 3, 6]
	print selectionSort(arr)

	#sort an array of strings using selection sort
	arr = ['paper', 'true', 'soap', 'floppy', 'flower']
	print selectionSort(arr)
