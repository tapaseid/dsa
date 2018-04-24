# 0-1 knapsack problem

def knapsack(w, wt, v, n):
	# time complexity O(2^n)
	# space complexity O(1)
	
	if w == 0 or n == 0:
		return 0
	if wt[n-1] > w:
		return knapsack(w, wt, v, n-1)
	else:
		return max(v[n-1] + knapsack(w - wt[n-1], wt, v, n-1), knapsack(w, wt, v, n-1))

# optimal solution
def knapSack(w, wt, v, n):
	# time complexity O(nw)
	# space complexity O(nw)

	# k = [[0 for x in range(w+1)] for y in range(n+1)]
	import numpy as np
	k = np.empty((n+1, w+1), dtype=object)
	for i in range(n+1):
		for j in range(w+1):
			if i == 0 or j == 0:
				k[i][j] = 0
			elif wt[i-1] > w:
				k[i][j] = k[i-1][j]
			else:
				k[i][j] = max(v[i-1] + k[i-1][j - wt[i-1]], k[i-1][j])
			# print "i = {}, j = {}, k[i][j] = {}".format(i, j, k[i][j])
	# print k
	return k[n][w]




def knapSack_test(W, wt, val, n, unique_no):
	# time complexity O(nW)
	# space complexity O(nW)

	K = [[0 for x in range(W+1)] for x in range(n+1)]

	# Build table K[][] in bottom up manner
	for i in range(n+1):
		for w in range(W+1):
			if i==0 or w==0:
				K[i][w] = 0
			elif wt[i-1] <= w:
				K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
			else:
				K[i][w] = K[i-1][w]

	res = K[n][W]
	L = [res]
	w = W
	for i in range(n, 0, -1):
	    if res == K[i-1][w]:
	        continue
	    else:
	        L.insert(0, unique_no[i-1])
	        res -= val[i-1]
	        w -= wt[i-1]
	return L


if __name__ == '__main__':
	v = [60, 100, 120]
	wt = [10, 20, 30]
	print knapSack(50, wt, v, 3)
	

	W = 300
	n = 3
	unique_no = [38, 21, 13]
	wt = [130, 280, 120]
	v = [500, 1800, 1500]
	print knapSack_test(W, wt, v, n, unique_no)
