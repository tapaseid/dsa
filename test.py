
# l = 100

# radars = [ [5, 10], [3, 25], [46, 99], [39, 40], [45, 50] ]

# border = 0
# radars.sort(key=lambda x: x[0])
# i, j = 0, 1
# while j < len(radars):
#       while j < len(radars) and radars[j][0] < radars[i][1]:
#           j += 1
#       if l >= border + max(radars[i][1], radars[j-1][1])-radars[i][0]:
#           border += max(radars[i][1], radars[j-1][1])-radars[i][0]
#           i = j
#       else: break
#       j += 1
# print border



import sys

def count_ways(arr, n, w):
    if w == 0:
        return 1
    if w < 0 or n == 0:
        return 0
    return count_ways(arr, n-1, w) + count_ways(arr, n, w-arr[n-1])

def count_ways_dp(arr, n, w):
    t = [[0]*n for _ in range(w+1)]
    for i in range(n):
        t[0][i] = 1
    for i in range(1, w+1):
        for j in range(n):
            x = t[i-arr[j]][j] if i - arr[j] >= 0 else 0
            y = t[i][j-1] if j >= 1 else 0
            t[i][j] = x+y
    for i in range(w+1):
        print t[i]
    return t[w][n-1]
 
arr = [1, 2, 3]
print count_ways_dp(arr, len(arr), 10)

sys.exit(0)




# First non repeating character in a stream of input
def first_repeating(s):
    repeated = [False]*256
    lookups = []

    for i in range(len(s)):
        # if not repeated[ord(s[i])]:
        if not s[i] in lookups:
        	if not repeated[ord(s[i])]:
        		lookups.append(s[i])
            	repeated[ord(s[i])] = True
        else:
            lookups.remove(s[i])
        if len(lookups):
            print lookups[0]
    print lookups
s = 'geeksforgeeksandgeeksquizfor'
# first_repeating(s)


# Find all permutations of a string!
def _helper(s_list, index, n):
	if index == n-1:
		print ''.join(s_list)
		return
	for i in range(index, n):
		if should_swap(s_list, index, i):
			s_list[index], s_list[i] = s_list[i], s_list[index]
			_helper(s_list, index+1, n)
			s_list[index], s_list[i] = s_list[i], s_list[index]

def should_swap(lst, l, i):
	for j in range(l, i):
		if lst[j] == lst[i]:
			return 0
	return 1

def string_permutation(s):
	n = len(s)
	s_list = list(s)
	_helper(s_list, 0, n)

# string_permutation('ABCA')


def permutations(word, r):
	n = len(word)
	tmp = [None]*r
	# print_r_combinations(word, tmp, 0, n, 0, r)
	test(word, tmp, 0, n, 0, r)

def test(word, tmp, s, e, i, r):
	if i == r:
		print tmp
		return
	if s >= e:
		return

	tmp[i] = word[s]
	test(word, tmp, s+1, e, i+1, r)
	test(word, tmp, s+1, e, i, r)

def print_r_combinations(word, tmp, s, e, i, r):
	if i == r:
		print ''.join(filter(None, tmp))
		return
	j = s
	while j < e:
		if e-j+1 >= r-i:
			tmp[i] = word[j]
			print_r_combinations(word, tmp, j+1, e, i+1, r)

		j +=1

# permutations('ABC', 2)


# Max no in sliding window of size k

def max_in_k_sliding_window(arr, k):
	n = len(arr)
	if n < k:
		print "Impossible!"
	t1 = []
	t2 = []
	for i in range(k):
		while t1 and arr[i] > arr[t1[-1]]:
			t1.pop()
		t1.append(i)
		while t2 and arr[i] < arr[t2[-1]]:
			t2.pop()
		t2.append(i)

	for i in range(k, n):
		print arr[t1[0]]+arr[t2[0]]
		if t1[0] < i-k+1:
			t1.pop(0)
		if t2[0] < i-k+1:
			t2.pop(0)

		while t1 and arr[i] > arr[t1[-1]]:
			t1.pop()
		t1.append(i)

		while t2 and arr[i] < arr[t2[-1]]:
			t2.pop()
		t2.append(i)

	print arr[t1[0]]+arr[t2[0]]

arr = [10, 5, 2, 7, 8, 7]
# max_in_k_sliding_window(arr, 3)




def f(a, b):
    if len(a) < len(b):
        return False
    if b == '':
        if a.lower() == a:
            return True
        else:
            return False
    if a[-1] == b[-1]:
        return f(a[:-1], b[:-1])
    else:
        if a[-1] == a[-1].upper():
            return False
        else:
            if a[-1].upper() != b[-1]:
                return f(a[:-1], b)
            else:
                return f(a[:-1]+a[-1].upper(), b) or f(a[:-1], b)
            
def abbreviation(a, b):
    if f(a, b):
        print "YES"
    else:
        print "NO"

# abbreviation('KabcX', 'KX')

import sys
def f(a, b, dp):
    if len(a) < len(b):
        return False
    if b == '':
        if a.lower() == a:
            return True
        else:
            return False
    if dp[len(a)][len(b)] != None:
        return dp[len(a)][len(b)];
    if a[-1] == b[-1]:
        dp[len(a)][len(b)] = f(a[:-1], b[:-1], dp)
        return dp[len(a)][len(b)]
    else:
        if a[-1] == a[-1].upper():
            return False
        else:
            if a[-1].upper() != b[-1]:
                dp[len(a)][len(b)] = f(a[:-1], b, dp)
            else:
                dp[len(a)][len(b)] = f(a[:-1]+a[-1].upper(), b, dp) or f(a[:-1], b, dp)
    return dp[len(a)][len(b)]

def abbreviation(a, b):
    # Complete this function
    dp = [[None]*(len(b)+2) for i in range(len(a)+2)]
    x = f(a, b, dp)
    if x:
        return "YES"
    return "NO"

def prime_factors(n):
    # Write your code here

    factors = []
    import math
    for i in range(2, int(math.sqrt(n))+1):
        while n%i == 0:
        	n /= i
        factors.append(i)
        print n
    if n != 1:
    	factor.append(n)
    return factors

print prime_factors(12)

