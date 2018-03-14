# Given an array of N elements and L and R, print the number of sub-arrays such that
# the value of the maximum array element in that subarray is at least L and at most R.

# Examples:
# Input : arr[] = {2, 0, 11, 3, 0}, L = 1, R = 10
# Output : 4 
# Explanation: the sub-arrays {2}, {2, 0}, {3} and {3, 0} have maximum in range 1-10.

# Input : arr[] = {3, 4, 1}, L = 2, R = 4 
# Output : 5
# Explanation: the sub-arrays are {3}, {4}, {3, 4}, {4, 1} and {3, 4, 1}

def _countSubarray(n):
	return n*(n+1)/2

# Time complexity ---> O(n)
def count_subarrays(arr, n, L, R):
	res = 0
	exc = 0 # smaller than L
	inc = 0 # smaller than or equal to R

	for i in range(n):

		# if element is grater than R
		if arr[i] > R:
			res += _countSubarray(inc) - _countSubarray(exc)
			inc = 0
			exc = 0

		# if element is smaller than L
		elif arr[i] < L:
			exc += 1
			inc += 1

		# if >= L and <= R
		else:
			res -= _countSubarray(exc)
			exc = 0
			inc += 1

	res += _countSubarray(inc) - _countSubarray(exc)
	return res

if __name__ == '__main__':
	# arr, L, R = [2, 0, 11, 3, 0], 1, 10
	arr, L, R = [3, 4, 1], 2, 4
	n = len(arr)

	print count_subarrays(arr, n, L, R)
