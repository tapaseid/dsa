# Count inversion in an array using merge sort

def _helper(arr, tmp, l, r):
	count = 0
	if l<r:
		m = (l+r)/2
		count = _helper(arr, tmp, l, m)
		count += _helper(arr, tmp, m+1, r)
		count += merge(arr, tmp, l, m, r)
	return count

def merge(arr, tmp, l, m, r):
	k = l
	i, j = l, m+1
	c = 0
	while i<=m and j<=r:
		if arr[i] < arr[j]:
			tmp[k] = arr[i]
			i += 1
		else:
			tmp[k] = arr[j]
			j += 1
			c += m+1-i
		k += 1
	while i<=m:
		tmp[k] = arr[i]
		i += 1
		k += 1
	while j<=r:
		tmp[k] = arr[j]
		j += 1
		k += 1

	for i in range(l, r+1):
		arr[i] = tmp[i]
	return c

# Time Complexity: O(n*log(n))
# Auxiliary Space: O(n)
def count_inversion(arr):
	n = len(arr)
	tmp = [None]*n
	return _helper(arr, tmp, 0, n-1)


if __name__ == '__main__':
	# arr = [1, 20, 6, 4, 5]
	# arr = [1, 3, 5, 2, 4, 6]
	arr = [7, 1, 3, 2, 4, 5, 6]
	print count_inversion(arr)
