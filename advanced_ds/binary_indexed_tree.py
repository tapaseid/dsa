# Binary indexed tree or fenwick tree

def getSum(BITTree, i):
	s = 0
	i += 1
	while i > 0:
		s += BITTree[i]
		i -= i&(-i) # Move index to parent node in getSum View
	return s

def updateBIT(BITTree, n, i, v):
	i += 1
	while i <= n:
		BITTree[i] += v
		i += i&(-i) # Update index to that of parent in update View

def constructBIT(arr, n):
	BITTree = [0]*(n+1)
	for i in range(n):
		updateBIT(BITTree, n, i, arr[i])

	# for i in range(1, n+1):
	# 	print BITTree[i],

	return BITTree

#####################APPLICATIONS######################
# 1. Count inversions in an array
# 2. Two dimensional BIT or Fenwick tree
# 3. Counting Tringles in a Rectangular space
#######################################################

if __name__ == '__main__':
	arr = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
	n = len(arr)
	BITTree = constructBIT(arr, n)
	print getSum(BITTree, 5)
	updateBIT(BITTree, n, 1, 5)
	print getSum(BITTree, 5)

