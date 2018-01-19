# We have to find out the maximum sum increasing sequence.
# Slightly different from LIS.

def max_sum_IS(arr):
	# Time complexity O(n*n)

	n = len(arr)
	s = [i for i in arr]

	for i in range(1, n):
		for j in range(i):
			if arr[j] < arr[i]:
				s[i] = max(s[i], s[j] + arr[i])

	mx = s[0]
	for i in range(1, n):
		if s[i] > mx:
			mx = s[i]

	return mx

def max_sum_IS_efficient(arr):
	pass

if __name__ == '__main__':
	arr = [1, 101, 2, 3, 100, 4, 5]
	print max_sum_IS(arr)
