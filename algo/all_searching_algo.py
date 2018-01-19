# Important searching algos are
# 1. Linear search ---> O(n)
# 2. Binary search ---> O(log n)
# 3. Jump search ---> O(sqrt(n))
# 4. Interpolation search ---> in worst case O(n), but if uniformly distributed O(log log n)
# 5. Exponential search ---> O(log n)
# 6. Ternary search ---> O(log n), base 3
# 7. Fibonacci search ---> O(log n)

def linearSearch(arr, key):
	for i in range(len(arr)):
		if arr[i] == key:
			return i
	return -1

def binarySearch(arr, l, r, key):

	# if l <= r:
	# 	mid = (l+r)/2
	# 	if arr[mid] == key:
	# 		return mid
	# 	elif arr[mid] < key:
	# 		return binarySearch(arr, mid+1, r, key)
	# 	else:
	# 		return binarySearch(arr, l, mid-1, key)
	# return -1

	while l <= r:
		mid = (l+r)/2
		if arr[mid] == key: return mid
		elif arr[mid] < key: l = mid+1
		else: r = mid-1
	return -1

def jumpSearch(arr, n, key):
	import math
	step = int(math.sqrt(n))
	prev = 0

	while arr[min(step, n) - 1] < key:
		prev = step
		step += int(math.sqrt(n))
		if prev >= n:
			return -1

	while arr[prev] < key:
		prev += 1
		if prev == min(step, n):
			return -1

	if arr[prev] == key:
		return prev

	return -1

def interpolationSearch(arr, n, key):
	lo = 0
	hi = n - 1

	while lo <= hi and key >= arr[lo] and key <= arr[hi]:

		# probe equation
		pos = lo + int((float(hi - lo)/(arr[hi] - arr[lo])) * (key - arr[lo]))
		
		if arr[pos] == key: return pos
		if arr[pos] < key: lo = pos + 1
		else: hi = pos - 1
	
	return -1

def exponentialSearch(arr, n, key):
	if arr[0] == key:
		return 0
	i = 1
	while i < n and arr[i] <= key:
		i *= 2
	return binarySearch(arr, i/2, min(i, n-1), key)

def ternarySearch(arr, l, r, key):
	if l <= r:
		mid1 = l + (r-l)/3
		mid2 = mid1 + (r-l)/3
		if arr[mid1] == key: return mid1
		if arr[mid2] == key: return mid2
		if arr[mid1] > key: return ternarySearch(arr, l, mid1-1, key)
		if arr[mid2] < key: return ternarySearch(arr, mid2+1, r, key)
		return ternarySearch(arr, mid1+1, mid2-1, key)
	return -1

def fibonacciSearch(arr, n, key):
	fibM2 = 0
	fibM1 = 1
	fibM = fibM2 + fibM1
	offset = 0
	
	while fibM < n:
		fibM2 = fibM1
		fibM1 = fibM
		fibM = fibM2 + fibM1
	
	while fibM >1:
		i = min(offset+fibM2, n-1)
		if arr[i] < key:
			fibM = fibM1
			fibM1 = fibM2
			fibM2 = fibM - fibM1
			offset = i
		elif arr[i] > key:
			fibM = fibM2
			fibM1 = fibM1 - fibM2
			fibM2 = fibM - fibM1
		else: return i
	if fibM1 and arr[offset] == key: return offset
	return -1



if __name__ == '__main__':
	arr = [1, 2, 4, 5, 9, 12, 20]
	n = len(arr)
	arr2 = [5, 2, 7, 20, 3, 12, 19]
	# print linearSearch(arr2, 3)
	# print binarySearch(arr, 0, n-1, 12)
	# print jumpSearch(arr, n, 5)
	# print interpolationSearch(arr, n, 1)
	# print exponentialSearch(arr, n, 12)
	# print ternarySearch(arr, 0, n-1, 12)
	print fibonacciSearch(arr, n, 12)
