# insertion sort

def insertionSort(arr):
	n = len(arr)
	if n == 0 or n == 1:
		return
	for j in range(1, n):
		key = arr[j]
		i = j-1
		while i >= 0 and arr[i] > key:
			arr[i+1] = arr[i]
			i -= 1 
		arr[i+1] = key
	return arr

def binary_util_search(arr, key, l, r):
	if l == r:
		if arr[l] > key: return l
		else: return l+1
	if l > r: return l
	
	mid = (l+r)/2
	if arr[mid] > key: return binary_util_search(arr, key, l, mid-1)
	if arr[mid] < key: return binary_util_search(arr, key, mid+1, r)
	else: return mid

def insertionSort_using_binary_search(arr):
	n = len(arr)
	if n == 0 or n == 1:
		return
	for j in range(1, n):
		key = arr[j]
		i = binary_util_search(arr, key, 0, j-1)
		arr = arr[:i] + [key] + arr[i:j] + arr[j+1:]
	return arr

# driver method
if __name__ == '__main__':
	arr = [8, 2, 4, 9, 3, 6]
	# print insertionSort(arr)
	print insertionSort_using_binary_search(arr)

