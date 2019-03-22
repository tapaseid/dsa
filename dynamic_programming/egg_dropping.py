# Egg dropping problem.

# Recursive
# Time complexity: O(exp)
def attempts_req(f, e):
	if f == 1 or f == 0:
		return f
	if e == 1:
		return f

	import sys
	mn = sys.maxint
	for i in range(1, f+1):
		res = max(attempts_req(i-1, e-1), attempts_req(f-i, e))
		mn = min(mn, res)
	return 1 + mn

# Dynamic programming
# Time complexity: O(e*f*f)
def min_no_of_attempts_required(floors, eggs):
	t = [[None]*(floors+1) for _ in range(eggs+1)]
	for j in range(floors+1):
		t[1][j] = j
	for i in range(2, eggs+1):
		for j in range(floors+1):
			if i>j:
				t[i][j] = t[i-1][j]
			else:
				t[i][j] = 1 + min(max(t[i-1][k-1], t[i][j-k]) for k in range(1, j+1))
	return t[eggs][floors]

# Binomial coefficient and binary search solution
# Time complexity: O(e*logf)
def min_trials(f, e):
	low, high = 1, f

	while low < high:
		mid = (low+high)/2
		if binomial_coeff(mid, f, e) < f:
			low = mid+1
		else:
			high = mid

	return low

def binomial_coeff(m, f, e):
	sm = 0
	term = 1
	i = 1
	while i<=e and sm<f:
		term *= m-i+1
		term /= i
		sm += term
		i += 1
	return sm

if __name__ == '__main__':
	floors = 10
	eggs = 2
	print "Recursive: ", attempts_req(floors, eggs)
	print "Dynamic programming: ", min_no_of_attempts_required(floors, eggs)
	print "Using Binomial coefficient: ", min_trials(floors, eggs)
