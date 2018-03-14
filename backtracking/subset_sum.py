# Subset sum problem is to find subset of elements that are selected from a
# given set whose sum adds up to a given number K.
# We are considering the set contains non-negative values.
# It is assumed that the input set is unique (no duplicates are presented).

def _helper(arr, n, subset, k, index):
	if index == n:
		if checkSum(subset) <= k:
			print _filter_set(subset)
		return

	subset[index] = None
	_helper(arr, n, subset, k, index+1)
	subset[index] = arr[index]
	_helper(arr, n, subset, k, index+1)

def checkSum(subset):
	return sum(_filter_set(subset))

def _filter_set(lst):
	return filter(None, lst)

def generate_subsetSum(arr, n, k):
	subset = [None]*n
	_helper(arr, n, subset, k, 0)

if __name__ == '__main__':
	arr = [10, 7, 5, 18, 12, 20, 15]
	k = 35
	n = len(arr)
	generate_subsetSum(arr, n, k)
