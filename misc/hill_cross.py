# Suppose we have n hills with some cost and there is a tunnel for every hills.
# If we cross a hill through tunnel(cost is 0), next time we have to climb(cost is hill's cost).
# Compute minimum cost.

def hills_crossing_cost(hills, end):
	# time complexicity: O(2^n)
	if end == 0:
		return 0
	if end == 1:
		return min(hills[0], hills[1])

	return min(hills[end] + hills_crossing_cost(hills, end-1),
		hills[end-1] + hills_crossing_cost(hills, end-2))

def hills_dp(hills):
	# time complexicity: O(n)
	# solution using dynamic programming  
	n = len(hills)

	# intialize the table
	t = [0]*(n+1)

	for i in range(1, n):
		result = min(hills[i]+t[i], hills[i-1]+t[i-1])
		t[i+1]= result

	return t[n]

if __name__ == '__main__':
	# hills = [4, 2, 1, 5, 3]
	hills = [4, 2, 1, 5, 6]
	#print hills_crossing_cost(hills, len(hills)-1)
	print hills_dp(hills)
