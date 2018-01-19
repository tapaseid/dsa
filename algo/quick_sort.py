# Quick sort

def quikSort(arr, l, r):
	if l < r:
		pi = partition(arr, l, r)
		quikSort(arr, l, pi-1)
		quikSort(arr, pi+1, r)
	return arr

def partition(arr, l, r):
	pivot = arr[r]

	i = l - 1
	for j in range(l, r):
		if arr[j] <= pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i+1], arr[r] = pivot, arr[i+1]
	return i+1

def quickSortItrative(arr, l, r):
	if l < r:
		size = r-l+1
		stack = [0]*size

		top = -1

		top += 1
		stack[top] = l
		top += 1
		stack[top] = r

		while top >= 0:
			r = stack[top]
			top -= 1
			l = stack[top]
			top -= 1

			p = partition(arr, l, r)

			if p-1 > l:
				top += 1
				stack[top] = l
				top += 1
				stack[top] = p-1

			if p+1 < r:
				top += 1
				stack[top] = p+1
				top += 1
				stack[top] = r

	return arr


# driver method
if __name__ == '__main__':
	arr = [8, 2, 6, 4, 9, 3, 6]
	print quickSortItrative(arr, 0, len(arr)-1)
