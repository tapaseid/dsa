# Left rotate a sorted array

def leftRotate(arr, d):
	# Time complexity O(n)
	
	n = len(arr)
	reverse(arr, 0, d)
	reverse(arr, d+1, n-1)
	reverse(arr, 0, n-1)
	return arr

def reverse(arr, start, end):
	while start < end:
		arr[start], arr[end] = arr[end], arr[start]
		start += 1
		end -= 1

# driver method
if __name__ == '__main__':
	arr = [3, 4, 5, 1, 2]
	print leftRotate(arr, 2)
