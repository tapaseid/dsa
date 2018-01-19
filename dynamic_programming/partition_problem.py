# Partition problem is to determine whether a given set can be partitioned into
# two subsets such that the sum of elements in both subsets is same.


TEST_INPUT = [
				[],
				[1],
				[1, 2],
				[1, 2, 3],
				[1, 2, 3, 4],
				[1, 2, 3, 4, 5],
				[1, 2, 3, 4, 5, 6],
				[1, 2, 3, 4, 5, 6, 7],
			 ]

TEST_OUTPUT = [
				True,
				False,
				False,
				True,
				True,
				False,
				False,
				True
			  ]

def checkPartition(arr, n, sum2):
	# Time complexity O(2^n)

	#base cases
	if sum2 == 0: return True
	if n == 0 and sum2 != 0: return False

	if arr[n-1] > sum2:
		return checkPartition(arr, n-1, sum2)
	return checkPartition(arr, n-1, sum2) or checkPartition(arr, n-1, sum2-arr[n-1])


def checkPartitionEfficient(arr, n, sum2):
	# Time complexity O(sum*n)
	# Space complexity O(sum*n)

	# create part[n+1][sum2+1]
	part = [[0 for j in range(sum2+1)] for i in range(n+1)]
	for i in range(n+1):
		part[i][0] = True
	for i in range(1, sum2+1):
		part[0][i] = False

	for i in range(1, n+1):
		for j in range(1, sum2+1):
			if j < arr[i-1]:
				# print"IF"
				part[i][j] = part[i-1][j]
			else:
				# print "ELSE"
				part[i][j] = part[i-1][j] or part[i-1][j-arr[i-1]]

	# # To print the table
	# for i in range(n+1):
	# 	for j in range(sum2+1):
	# 		print "{}\t".format(part[i][j]),
	# 	print

	return part[n][sum2]

def hasPartition(arr):
	n = len(arr)

	#initial cases
	if n == 0: return True
	if n == 1: return False
	sum1 = 0
	for i in range(n):
		sum1 += arr[i]
	if sum1%2 != 0: return False

	return checkPartitionEfficient(arr, n, sum1/2)

def main():
	for i in range(len(TEST_INPUT)):
		print "Running test case {}:...".format(i+1)
		assert TEST_OUTPUT[i] == hasPartition(TEST_INPUT[i])
		# print hasPartition(TEST_INPUT[i])

	print "All test cases passed!"

if __name__ == '__main__':
	main()
