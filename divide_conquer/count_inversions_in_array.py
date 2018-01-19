# Count inversion in an array using merge sort

def merge(arr, l, mid, r):
	n1 = mid-l+1
	n2 = r-mid
	L = [0]*n1
	R = [0]*n2
	for i in range(n1):
		L[i] = arr[l+i]
	for i in range(n2):
		R[i] = arr[mid+1+i]
	i = j = c = 0
	k = l

	while i<n1 and j<n2:
		if L[i] < R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
			c += n1-i
		k += 1
	while i<n1:
		arr[k] = L[i]
		i += 1
		k += 1
	while j<n2:
		arr[k] = R[j]
		j += 1
		k += 1
	return c


def mergeSortUtil(arr, l, r):
	inv_count = 0
	if l < r:
		mid = (l+r)/2
		inv_count = mergeSortUtil(arr, l, mid)
		inv_count += mergeSortUtil(arr, mid+1, r)
		inv_count += merge(arr, l, mid, r)
		# print "IC:", inv_count
	return inv_count

if __name__ == '__main__':
	arr = [1, 20, 6, 4, 5]
	# arr = [1, 3, 5, 2, 4, 6]
	print mergeSortUtil(arr, 0, len(arr)-1)
