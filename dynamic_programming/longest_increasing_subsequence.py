# Longest increasing subsequence

global maximum

def _lis(arr, n):
    global maximum
    
    #Base case
    if n == 1:
        return 1

    maxEndingHere = 1
    for i in range(1, n):
        res = _lis(arr, i)
        if arr[i-1] < arr[n-1] and res+1 > maxEndingHere:
            maxEndingHere = res+1
    maximum = max(maximum, maxEndingHere)
    return maxEndingHere

def LIS_recursion(arr):
    # Naive aproach

    global maximum
    n = len(arr)
    maximum = 1
    _lis(arr, n)
    return maximum

def LIS_dp(arr):
    # Using tabulation
    # Time complexity O(n*n)

    n = len(arr)
    lis = [1]*n
    for i in range(1, n):
    	for j in range(i):
    		if arr[j] < arr[i]:
    			lis[i] = max(lis[i], lis[j] + 1)
    mx = 1
    for i in range(n):
    	if lis[i] > mx:
    		mx = lis[i]
    return mx


def LIS_dp_efficient(arr):
	# time complexity O(n*log(n))
	n = len(arr)
	s = []

	s.append(arr[0])
	for i in range(1, n):
		if arr[i] > s[-1]:
			s.append(arr[i])
		else:
			index = ceilIndex(arr, s, i)
			s[index] = arr[i]

	return len(s)

def ceilIndex(arr, s, i):
	low = 0
	high = len(s) - 1

	while high > low:
		mid = (high+low)/2
		if s[mid] < arr[i]:
			low = mid+1
		else:
			high = mid

	return high

if __name__ == '__main__':
    # arr = [10, 22, 9, 33, 21, 50, 41, 60]
    # print "Length of LIS is:", LIS_dp(arr)

    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    print LIS_dp_efficient(arr)
