
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

def _get_contiguous_subsets(arr):
    n = len(arr)
    res = []
    for i in range(1, n+1):
        l, r = 0, i
        while r<=n:
            res.append(arr[l:r])
            l += 1
            r += 1
    return res
    
def _get_score(all_subsets, i):
    import math
    score = 0
    for ele in all_subsets:
        m = len(ele)
        for j in range(1, m+1):
            score += ele[j-1]*int(math.pow(j, i))
    return score

def max_power(all_subsets, k):
    power = 0
    for i in range(1,k+1):
        power += _get_score(all_subsets, i)
    return power%1000000007

def new_fun(all_subsets, k, n):
    import math
    pow_i = [0]*n
    for index in range(n):
        for i in range(1, k+1):
            pow_i[index] += int(math.pow(index+1, i))
            pow_i[index] %= 1000000007
    score = 0
    for ele in all_subsets:
        m = len(ele)
        for i in range(m):
            score += ele[i]*pow_i[i]
            score %= 1000000007
    return score

          
def _helper(n, x, y, c, d, e1, e2, f):
    arr = [None]*n
    first = (x+y)%f
    arr[0] = first
    for i in range(1, n):
        tmp_x = (c*x + d*y + e1)%f
        tmp_y = (d*x + c*y + e2)%f
        arr[i] = (tmp_x+tmp_y)%f
        x, y = tmp_x, tmp_y
    return arr
  
t = int(raw_input())
i = 0
while i<t:
    n, k, x1, y1, c, d, e1, e2, f = map(int, raw_input().strip().split())
    arr = _helper(n, x1, y1, c, d, e1, e2, f)
    all_subsets = _get_contiguous_subsets(arr)
    # print arr, all_subsets
    # new_fun(all_subsets, k, n)
    print "Case #{}: {}".format(i+1,new_fun(all_subsets, k, n))
    i += 1

sys.exit(0)

def max_beauty(arr, n):
    res = 0
    total_index = n/2+1 if n%2 else n/2
    score = 0
    l = 0
    r = total_index
    for i in range(r):
        score += arr[i]
    res = max(res, score)
    while r < n:
        score -= arr[l]
        l += 1
        score += arr[r]
        r += 1
        res = max(res, score)
    return res
    
t = int(raw_input())
i = 0
while i<t:
    n = int(raw_input())
    arr = map(int, list(raw_input().strip()))
    print "Case #{}: {}".format(i+1, max_beauty(arr, n))
    i += 1


sys.exit(0)

def _is_contains_check(st, rules):
    for rule in rules:
        if st[:len(rule)] == rule:
            return True
    return False

def count(n, rules):
    st = 'R'*n
    q = []
    index = 0
    q.append((st, index))
    count = 0
    while q:
        st, index = q.pop(0)
        if not _is_contains_check(st, rules):
            count += 1
        if index < n:
            for i in range(index, n):
                tmp = st
                tmp = tmp[:i] + 'B' + tmp[i+1:]
                q.append((tmp, i+1))
    return count 
    
if __name__ == '__main__':
    # n, k = map(int, raw_input().split())
    # rules = []
    # for i in range(k):
    #     rules.append(raw_input())
        
    # print count(n, rules)

    t = int(raw_input())
    i = 1
    while i<=t:
        n, k = map(int, raw_input().split())
        rules = []
        for i in range(k):
            rules.append(raw_input())
            
        print "Case #{}: {}".format(i, count(n, rules))
        i += 1

sys.exit(0)

def maxRegion(grid):
    m = len(grid)
    n = len(grid[0])

    mx_count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                print i, j, grid
                x, y= i, j
                count = [1]
                dfs(grid, count, x, y, m, n)
                print count
                mx_count = max(mx_count, count[0])
    return mx_count
def dfs(grid, count, i, j, m, n):
    # import pdb
    # pdb.set_trace()
    if grid[i][j] == 0 or not(i>=0 and i<m and j>=0 and j<n):
        return 0
    row = [-1, -1, -1, 0, 0, 1, 1, 1]
    col = [-1, 0, 1, -1, 1, -1, 0, 1]

    grid[i][j] = 0
    for p in range(8):
        r = i+row[p]
        c = j+col[p]
        if r>=0 and r<m and c>=0 and c<n and grid[r][c]==1:
            count[0] += 1
            dfs(grid, count, r, c, m, n)

grid = [
        [1, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 1],
        [1, 0, 0, 0]
       ]
print maxRegion(grid)
sys.exit(0)

def subset(lst):
    n = len(lst)
    tmp = [None]*n
    _helper(lst, tmp, 0, n)
def _helper(lst, tmp, index, n):
    if index == n:
        print filter(None, tmp)
        return
    tmp[index] = None
    _helper(lst, tmp, index+1, n)
    tmp[index] = lst[index]
    _helper(lst, tmp, index+1, n)

subset([1, 2, 3])
sys.exit(0)


def optimalUtilization(deviceCapacity, foregroundAppList, backgroundAppList):
    # WRITE YOUR CODE HERE
    m = len(foregroundAppList)
    n = len(backgroundAppList)
    res = []
    tmp = None
    i = 0
    j = n-1
    curr_diff = 10000000000
    
    while i < m and j >= 0:
        if foregroundAppList[i][1] + backgroundAppList[j][1] == deviceCapacity:
            res.append([foregroundAppList[i][0], backgroundAppList[j][0]])
            if tmp:
                tmp = None
            i += 1
            j -= 1
        else:
            if foregroundAppList[i][1] + backgroundAppList[j][1] < deviceCapacity:
                if abs(foregroundAppList[i][1] + backgroundAppList[j][1] - deviceCapacity) < curr_diff:
                    tmp = [foregroundAppList[i][0], backgroundAppList[j][0]]
                    curr_diff = abs(foregroundAppList[i][1] + backgroundAppList[j][1] - deviceCapacity)
                i += 1
            else:
                if tmp:
                    res.append(tmp)
                    tmp = None
                    i += 1
                j -= 1
    if tmp:
        res.append(tmp)
    return res

# foregroundAppList = [[1, 3], [2, 5], [3, 7], [4, 10]]
# backgroundAppList = [[1, 2], [2, 3], [3, 4], [4, 5]]
foregroundAppList = [[1, 2], [2, 4], [3, 6]]
backgroundAppList = [[1, 2]]

print optimalUtilization(7, foregroundAppList, backgroundAppList)
def euclidean(pair):
    import math
    return math.sqrt(pair[0]*pair[0] + pair[1]*pair[1])
def nearestVegetarianRestaurant(totalRestaurants, allLocations, numRestaurants):
    # WRITE YOUR CODE HERE
    for i in range(totalRestaurants-1):
        swap = False
        for j in range(totalRestaurants-1-i):
            if euclidean(allLocations[j]) > euclidean(allLocations[j+1]):
                allLocations[j], allLocations[j+1] = allLocations[j+1], allLocations[j]
                swap = True
        if not swap:
            break
    # print allLocations
    return allLocations[:numRestaurants]

print nearestVegetarianRestaurant(3, [[1, 2], [3, 4], [1, -1]], 2)
sys.exit(0)

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

