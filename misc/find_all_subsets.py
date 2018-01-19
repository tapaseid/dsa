# Given a set, find all subsets

import math, time

def find_all_subsets(s):
	# Time complexity O(n * 2^n)
	n = len(s)

	for i in range(int(math.pow(2, n))):
		subset = []
		for j in range(n):
			if i&(1<<j):
				subset.append(s[j])
		print subset

def _helper(s, n, subset, i):
	if i == n:
		_print_set(subset)

	else:
		subset[i] = None
		_helper(s, n, subset, i+1)
		subset[i] = s[i]
		_helper(s, n, subset, i+1)

def _print_set(subset):
	print filter(None, subset)

def all_subsets(s):

	n = len(s)
	subset = [None]*n

	_helper(s, n, subset, 0)

if __name__ == '__main__':
	s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
	
	t0 = time.clock()
	find_all_subsets(s)
	print "Time taken1:", time.clock() - t0
	
	t1 = time.clock()
	all_subsets(s)
	print "Time taken2:",time.clock() - t1
