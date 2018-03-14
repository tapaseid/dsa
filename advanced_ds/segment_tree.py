# Query for minimum value of given range
# Construct segment tree to get Range Minimum Query

import sys
from math import log, ceil

MX = sys.maxint

def find_minimum_RMQ(st, qlow, qhigh, low, high, pos):
	if qlow > high or qhigh < low: # no overlap
		return MX
	if qlow <= low and qhigh >= high: # total overlap
		return st[pos]

	mid = (low+high)/2
	return min(find_minimum_RMQ(st, qlow, qhigh, low, mid, 2*pos+1),
		find_minimum_RMQ(st, qlow, qhigh, mid+1, high, 2*pos+2))

def updateValueUtil(st, ss, se, index, diff, pos):

	# Base case
	if index < ss or index > se:
		return

	st[pos] += diff
	if ss != se:
		mid = (ss+se)/2
		updateValueUtil(st, ss, mid, index, diff, 2*pos+1)
		updateValueUtil(st, mid+1, se, index, diff, 2*pos+2)

def updateValue(arr, st, n, index, new_value):
	if index < 0 or index > n-1:
		print "Invalid index!"
		return

	diff = new_value - arr[index]
	arr[index] = new_value
	updateValueUtil(st, 0, n-1, index, diff, 0)

def constructSTUtil(arr, st, low, high, pos):
	if low == high:
		st[pos] = arr[low]
		return
	mid = (low+high)/2
	constructSTUtil(arr, st, low, mid, 2*pos+1)
	constructSTUtil(arr, st, mid+1, high, 2*pos+2)
	st[pos] = min(st[2*pos+1], st[2*pos+2])

def constructST(arr, n):
	x = int(ceil(log(n, 2)))
	max_size = 2*pow(2, x)-1
	st = [MX]*max_size
	constructSTUtil(arr, st, 0, n-1, 0)
	return st

def find_min(st, n, qlow, qhigh):

	# Use recursive utility function to get min value in between the given range
	return find_minimum_RMQ(st, qlow, qhigh, 0, n-1, 0)


######################## Lazy propagation ###########################

def updateRange_LP_util(st_lp, lazy, ss, se, us, ue, value, pos):
	if ss > se or ss > ue or se < us: # out of range
		return

	if ss >= us and se <= ue: # current segment is fully in update range
		st_lp[pos] += value
		if ss != se:
			lazy[2*pos+1] += value
			lazy[2*pos+2] += value
		return

	mid = (ss+se)/2
	updateRange_LP_util


def updateRange_LP(arr, st_lp, lazy, n, us, ue, value):
	for i in range(us, ue+1):
		arr[i] += value
	updateRange_LP_util(st_lp, lazy, 0, n-1, us, ue, value, 0)

def find_minimum_RMQ_LP(st_lp, qlow, qhigh, low, high, pos):
	pass

def find_min_LP(st_lp, n, qlow, qhigh):
	return find_minimum_RMQ_LP(st_lp, qlow, qhigh, 0, n-1, 0)

#######################################################################


def main():
	# arr = [-1, 2, 4, 0]
	arr = [1, 2, 3, 4, 5]
	n = len(arr)

	# Build segment tree from given array in O(n) time
	st = constructST(arr, n)

	print find_min(st, n, 1, 3)

	# Update value
	updateValue(arr, st, n, 1, 3)

	print find_min(st, n, 1, 3)

	#########################
	# Lazy propagation part #
	#########################
	lazy = [0]*len(st)




if __name__ == '__main__':
	main()
