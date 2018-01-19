# To find the minimum length unsorted subarray such that the whole array can be sorted.

def unsorted_subarray(arr, n):
	# time complexity O(n)
	for s in range(0, n-1):
		if arr[s] > arr[s+1]:
			break
	if s == n-2:
		print "array is already sorted!"
		return None, None
	for e in range(n-1, 0, -1):
		if arr[e] < arr[e-1]:
			break
	
	mx = mn = arr[s]
	for i in range(s+1, e+1):
		if arr[i] > mx:
			mx = arr[i]
		if arr[i] < mn:
			mn = arr[i]

	for i in range(0, s):
		if arr[i] > mn:
			s = i
			break

	for i in range(n-1, e, -1):
		if arr[i] < mx:
			e = i
			break

	return s, e


if __name__ == '__main__':
	# arr = [10, 20, 30, 25, 40, 32, 31, 35, 50, 60]
	# arr = [1, 2, 3, 4, 5, 7, 8, 9]
	arr = [7, 8, 9, 1, 2, 3, 4, 5]
	n = len(arr)
	s, e = unsorted_subarray(arr, n)
	if not(s is None or e is None):
		for i in range(s, e+1):
			print arr[i],
