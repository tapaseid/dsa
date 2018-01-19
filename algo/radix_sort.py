# Radix sort

def countSort(arr, exp):
	n = len(arr)
	output = [0]*n
	count = [0]*10

	for i in range(n):
		index = arr[i]/exp
		count[index%10] += 1

	for i in range(1, 10):
		count[i] += count[i-1]

	i = n-1
	while i >= 0:
		index = arr[i]/exp
		output[count[index%10]-1] = arr[i]
		count[index%10] -= 1
		i -= 1

	for i in range(n):
		arr[i] = output[i]

def radixSort(arr):
	max1 = max(arr)
	exp = 1
	while max1/exp > 0:
		countSort(arr, exp)
		exp *= 10
	return arr

if __name__ == '__main__':
	# arr = [8, 2, 4, 9, 3, 6]
	arr = [170, 25, 160, 2, 98, 12]
	print radixSort(arr)

