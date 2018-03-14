# Given a sequence, find the length of the longest palindromic subsequence in it.

def lps_util(s, l, r):

	# Base case 1
	if l == r:
		return 1
	# Base case 2
	if s[l]== s[r] and l+1 == r:
		return 2

	if s[l] == s[r]:
		return 2 + lps_util(s, l+1, r-1)
	return max(lps_util(s, l, r-1), lps_util(s, l+1, r))

def lps_recursive(s):
	n = len(s)
	return lps_util(s, 0, n-1)


# Time complexity ---> O(n*n)
# Space complexity ---> O(n*n)
def longest_palindromic_subsequence(s):
	n = len(s)
	t = [[None for i in range(n)] for _ in range(n)]

	for i in range(n):
		t[i][i] = 1

	for l in range(2, n+1): # l is the length of substring
		for i in range(n-l+1):
			j = i+l-1
			if s[i] == s[j]:
				t[i][j] = 2 if l == 2 else 2 + t[i+1][j-1]
			else:
				t[i][j] = max(t[i][j-1], t[i+1][j])

	return t[0][n-1]


# Time complexity ---> O(n*n)
# Space complexity ---> O(n)
def longest_palindromic_subsequence_optimized(s):
	n = len(s)
	t = [0]*n

	for i in range(n-1, -1, -1):
		back_up = 0

		for j in range(i, n):
			if j == i: # similarly as t[i][i] = 1
				t[j] = 1
			elif s[i] == s[j]: # similarly as t[i][i] = t[i+1][j-1] + 2
				tmp = t[j]
				t[j] = back_up + 2
				back_up = tmp
			else:  # similarly as t[j][j] = max(t[i][j-1], t[i+1][j])
				back_up = t[j]
				t[j] = max(t[j-1], t[j])

	return t[n-1]

if __name__ == '__main__':
	# s = 'agbdba'
	s = 'GEEKSFORGEEKS'
	print "Recursion:", lps_recursive(s)
	print "Dynamic Programming:", longest_palindromic_subsequence(s)
	print longest_palindromic_subsequence_optimized(s)
