# Counting sort

def countingSort(arr_str):
	n = len(arr_str)
	output = [0]*n
	count = [0]*256

	arr = [i for i in arr_str]
	for i in range(n):
		count[ord(str(arr[i]))] += 1

	for i in range(1, 256):
		count[i] += count[i-1]
	
	i = n-1
	while i >= 0:
		output[count[ord(str(arr[i]))]-1] = arr[i]
		count[ord(str(arr[i]))] -= 1
		i -= 1

	return "".join(output)

# driver method
if __name__ == '__main__':
	# arr = [8, 2, 6, 4, 9, 3, 6]
	# print countingSort(arr)

	arr_str = "geeksforgeeks"
	print countingSort(arr_str)
