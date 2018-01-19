# To find the largest sum of contiguous subarray of a given array

# Kadane's algorithm!
def maxSubArraySum(arr):
	n = len(arr)

	start = end = s = 0
	max_so_far = max_ending_here = 0
	for i in range(n):
		max_ending_here = max_ending_here + arr[i]
		if max_ending_here < 0:
			max_ending_here = 0
			s = i + 1 
		elif max_so_far < max_ending_here:
			max_so_far = max_ending_here
			start = s
			end = i

	# max_so_far = curr_max = arr[0]
	# for i in range(n):
	# 	curr_max = max(arr[i], curr_max + arr[i])
	# 	max_so_far = max(max_so_far, curr_max)
	print "subarray is:",
	for j in range(start, end+1):
		print arr[j],
	print 
	return max_so_far

if __name__ == '__main__':
	arr = [-2, -3, 4, -1, -2, 5, 1, -3]
	print maxSubArraySum(arr)
