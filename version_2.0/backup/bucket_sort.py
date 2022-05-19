import sys

# Function to sort arr[] of
# size n using bucket sort
def bucketSort( arr,  n):
     
    # -> Create n empty buckets
    buckets = [[] for i in range(n)]
 
    # -> Put list elements in their corresponding bucket
    for i in range(n):
        bucketIndex = int(n * arr[i]) # Index of bucket
        buckets[bucketIndex].append(arr[i])
 
    # -> Sort elements in individual buckets
    for i in range(n):
        buckets[i].sort()
 
    # -> Concatenate all buckets into list arr
    index = 0
    for i in range(n):
        for j in range(len(buckets[i])):
            arr[index] = buckets[i][j]
            index += 1
    
    # resultant sorted input sequence returned
    return arr


def main():
	arr = [0.45,0.12,0.89,0.49,0.41,0.32,0.67]
	# size of input array
	n = len(arr)
	# prints the given input sequence
	print("Given array is:")
	for i in range(n):
		print(arr[i])
	print()

	# bucketSort function called
	# arr is assigned to sorted input sequence
	arr = bucketSort(arr, n)

	#prints the resultant sorted sequence
	print("Sorted array is:")
	for i in range(n):
		print(arr[i])

    
if __name__ == '__main__':
    main()
