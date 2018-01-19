# Coin change problem.
import os, sys

def minCoinRequired(coins, m, value):
	# Time complexity O(exp)
	if value == 0:
		return 0
	result = sys.maxint
	for i in range(m):
		if coins[i] <= value:
			sub_res = minCoinRequired(coins, m, value-arr[i])
			if sub_res != sys.maxint and sub_res + 1 < result:
				result = sub_res + 1
	return result

def minCoinRequired1(coins, m, v):
	# using dp, time complexity O(mv)
	table = [sys.maxint for i in range(v+1)]
	table[0] = 0

	for i in range(1, v+1):
		for j in range(m):
			if coins[j] <= i:
				sub_res = table[i - coins[j]]
				# if sub_res != sys.maxint and sub_res + 1 < table[i]:
				# 	table[i] = sub_res + 1
				table[i] = min(table[i], sub_res + 1)
	# print table
	return table[v]


def count(arr, m, n):
	# Brute-force, simple recursion
	# Time complexity O(exp)
	if n == 0:
		return 1
	if n < 0:
		return 0
	if m <=0 and n >= 1:
		return 0
	return count(arr, m-1, n) + count(arr, m, n-arr[m-1])


def count1(arr, m, n):
	# Using dynamic programing
	# Time complexity O(mn)

	t = [[0 for i in range(m)] for j in range(n+1)]
	for i in range(m):
		t[0][i] = 1

	for i in range(1, n+1):
		for j in range(m):
			x = t[i-arr[j]][j] if i-arr[j] >= 0 else 0
			y = t[i][j-1] if j >= 1 else 0
			t[i][j] = x + y

	# print "T:", t
	return t[n][m-1]

def count2(arr, m, n):
	# Better than count1() according to space complexity.
	t = [0 for i in range(n+1)]
	t[0] = 1

	for i in range(m):
		for j in range(arr[i], n+1):
			t[j] += t[j-arr[i]]
	return t[n]

if __name__ == '__main__':
	# arr = [1,2, 3]
	arr = [9, 5, 6, 1]
	m = len(arr)
	# print count1(arr, m, 5)
	print minCoinRequired1(arr, m, 11)
