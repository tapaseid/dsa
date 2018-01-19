# Bucket sort

def isort(arr):
	n = len(arr)
	if n <= 1: return arr
	for j in range(1, n):
		key = arr[j]
		i = j-1
		while i>=0 and arr[i] > key:
			arr[i+1] = arr[i]
			i -= 1
		arr[i+1] = key
	return arr

def bucketSort(arr):
	n = len(arr)
	buckets = [[] for i in range(n)]

	for i in range(n):
		buckets[int(n*arr[i])].append(arr[i])
	
	out = []
	for buck in buckets:
		out += isort(buck)

	return out


if __name__ == '__main__':
	arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434, 0.15, 0.555]
	print bucketSort(arr)
