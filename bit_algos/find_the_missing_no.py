# You are given a list of n-1 integers and these integers are in the range of 1 to n.
# One of the integers is missing in the list.
# There are no duplicate in the list.

def findMissing(arr):
	n = len(arr)
	sum_all = ((n+1)*(n+2))/2
	for i in range(n):
		sum_all -= arr[i]

	return sum_all

def findMissing_XOR(arr):
	n = len(arr)
	x1 = arr[0]
	x2 = 1
	for i in range(1, n):
		x1 ^= arr[i]
	for i in range(2, n+2):
		x2 ^= i

	return x1^x2

if __name__ == '__main__':
	arr = [1, 2, 4, 6, 3, 7, 8]
	# print findMissing(arr)
	print findMissing_XOR(arr)
