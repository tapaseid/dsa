# Minimum number of swaps required to sort an array

# Time Complexity: O(n*log(n))
# Auxiliary Space: O(n)
def minimum_swaps(arr):
	n = len(arr)
	visit = [False]*n
	arrpos = list(enumerate(arr))
	arrpos.sort(key=lambda x: x[1])
	print arrpos
	count = 0
	for i in range(n):
		if visit[i] or arrpos[i][0] == i:
			continue

		cycle_size = 0
		val = i
		while not visit[val]:
			visit[val] = True
			val = arrpos[val][0]
			cycle_size += 1
		if cycle_size > 0:
			count += cycle_size-1
	return count

# arr = [1, 2, 3, 4]
# arr = [1, 20, 6, 4, 5]
arr = [1, 5, 4, 3, 2]

print minimum_swaps(arr)
