# Search an element from a reverse sorted array.

def search(arr, key):
	# Time complexity O(log n)
	
	n = len(arr)
	return _search(arr, 0, n-1, key)

def _search(arr, l, h, key):
	# Util method for search() 
	if l > h: return -1
	
	mid = (l + h)/2
	
	if arr[mid] == key: return mid

	if arr[l] <= arr[mid]:
		if arr[l] <= key and arr[mid] > key:
			return _search(arr, l, mid-1, key)
		return _search(arr, mid+1, h, key)

	if arr[mid] > key and arr[h] >= key:
		return _search(arr, mid+1, h, key)
	
	return _search(arr, l, mid-1, key)


if __name__ == '__main__':
	arr = [3, 4, 5, 1, 2]
	print search(arr, 1)
