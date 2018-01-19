# Least common subsequence problem.

def LCS_recursion(x, y, m, n):
	# Time complexity O(2^n)

	if m == 0 or n == 0:
		return 0
	elif x[m-1] == y[n-1]:
		return 1 + LCS_recursion(x, y, m-1, n-1)
	else:
		return max(LCS_recursion(x, y, m-1, n), LCS_recursion(x, y, m, n-1))

def LCS_dp(x, y):
	# Time complexity O(mn)
	# Space complexity O(mn)

	m = len(x)
	n = len(y)
	t = [[None]*(n+1) for _ in range(m+1)]

	for i in range(m+1):
		for j in range(n+1):
			if i == 0 or j == 0:
				t[i][j] = 0
			elif x[i-1] == y[j-1]:
				t[i][j] = 1 + t[i-1][j-1]
			else:
				t[i][j] = max(t[i][j-1], t[i-1][j])

	return t[m][n]


def LCS_dp_efficient(x, y):
	# Time complexity O(mn)
	# Space complexity O(n)

	m = len(x)
	n = len(y)
	t = [[None]*(n+1) for _ in range(2)]

	for i in range(m+1):
		b = i&1
		for j in range(n+1):
			if i == 0 or j == 0:
				t[b][j] = 0
			elif x[i-1] == y[j-1]:
				t[b][j] = t[1-b][j-1] + 1
			else:
				t[b][j] = max(t[1-b][j], t[b][j-1])

	return t[b][n]

if __name__ == '__main__':
	x = "AGGTAB"
	y = "GXTXAYB"
	# print LCS_recursion(x, y, len(x), len(y))
	print LCS_dp(x, y)
	print LCS_dp_efficient(x, y)
