# merge sort

def merge(arr, l, mid, r):
	n1 = mid-l+1
	n2 = r-mid
	L = [0]*n1
	R = [0]*n2
	for i in range(0, n1):
		L[i] = arr[l+i]
	for i in range(0, n2):
		R[i] = arr[mid+1+i]

	i = 0
	j = 0
	k = l

	while i<n1 and j<n2:
		if L[i]<R[j]:
			arr[k] = L[i]
			i +=1
		else:
			arr[k] = R[j]
			j += 1
		k += 1
	while i<n1:
		arr[k] = L[i]
		i += 1
		k += 1
	while j<n2:
		arr[k] = R[j]
		j += 1
		k += 1
	return arr


def mergeSort(arr, l, r):
	if l<r:
		mid = (r+l)/2
		mergeSort(arr, l, mid)
		mergeSort(arr, mid+1, r)
		return merge(arr, l, mid, r)
	return arr

# driver method
if __name__ == '__main__':
	arr = [8, 2, 4, 9, 3, 6]
	print mergeSort(arr, 0, len(arr)-1)
