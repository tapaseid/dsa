# Maximum difference between two elements such that
# larger element appears after the smaller number

def MAX_DIFF_naive(arr):
	# Naive aproach
	# Time complexity O(n*n)

	n = len(arr)
	max_diff = arr[1] - arr[0]

	for i in range(1, n):
		for j in range(i+1, n):
			if arr[j] - arr[i] > max_diff:
				max_diff = arr[j] - arr[i]

	return max_diff

def Max_Diff(arr):
	# Time complexity O(n)
	# Space complexity O(1)

	n = len(arr)
	max_diff = arr[1]- arr[0]
	min_element = arr[0]

	for i in range(1, n):
		if arr[i] - min_element > max_diff:
			max_diff = arr[i] - min_element

		if arr[i] < min_element:
			min_element = arr[i]

	return max_diff

def Max_Diff_another(arr):
	# Time complexity O(n)
	# Space complexity O(1)

	n = len(arr)
	max_diff = -1
	max_right = arr[n-1]

	for i in range(n-2, -1, -1):
		if arr[i] > max_right:
			max_right = arr[i]
		else:
			diff = max_right - arr[i]
			if diff > max_diff:
				max_diff = diff

	return max_diff

def Max_Diff_tricky(arr):
	# Time complexity O(n)
	# Space complexity O(n)

	n = len(arr)
	d = [0]*(n-1)

	for i in range(n-1):
		d[i] = arr[i+1] - arr[i]

	max_diff = d[0]
	for i in range(1, n-1):
		if d[i-1] > 0:
			d[i] += d[i-1]
		if d[i] > max_diff:
			max_diff = d[i]

	return max_diff

def Max_Diff_tricky_another(arr):
	# Time complexity O(n)
	# Space complexity O(1)

	n = len(arr)
	diff = arr[1] - arr[0]
	curr = diff
	max_diff = curr

	for i in range(1, n-1):
		diff = arr[i+1] - arr[i]
		if curr > 0:
			curr += diff
		else:
			curr = diff

		if curr > max_diff:
			max_diff = curr

	return max_diff

if __name__ == '__main__':
	arr = [110, 1, 2, 90, 10, 100]
	# print MAX_DIFF_naive(arr)
	# print Max_Diff(arr)
	# print Max_Diff_another(arr)
	# print Max_Diff_tricky(arr)
	print Max_Diff_tricky_another(arr)
