# Maximum profit by buying and selling a share at most k times.

import sys

def maxProfit(stock, k):
	# Time complexity O(k*n*n)
	if k == 0 or len(stock) < 2:
		return 0

	n = len(stock)
	t = [[0 for i in range(n)] for _ in range(k+1)]

	for i in range(1, k+1):
		for j in range(1, n):
			t[i][j] = max(t[i][j-1], max([stock[j] - stock[m] + t[i-1][m] for m in range(j)]))

	return t[k][n-1]

def maxProfitEfficient(stock, k):
	# Time complexity O(k*n)
	if k == 0 or len(stock) < 2:
		return 0

	n = len(stock)
	t = [[0 for i in range(n)] for _ in range(k+1)]

	for i in range(1, k+1):
		maxDiff = - sys.maxint
		for j in range(1, n):
			maxDiff = max(maxDiff, t[i-1][j-1] - stock[j-1])
			t[i][j] = max(t[i][j-1], stock[j] + maxDiff)
	# print t
	print_Buy_Sell_Days(stock, t)
	return t[k][n-1]

def print_Buy_Sell_Days(stock, t):
	transaction = len(t) - 1
	day = len(t[0]) - 1
	stack = []

	while True:
		if transaction == 0 or day == 0:
			break
		if t[transaction][day] == t[transaction][day-1]: # didn't sell
			day -= 1
		else:
			stack.append(day)  # sold
			max_diff = t[transaction][day] - stock[day]
			for k in range(day-1, -1, -1):
				if t[transaction-1][k] - stock[k] == max_diff:
					stack.append(k) #bought
					transaction -= 1
					day = k
					break
		# print "Trans: {}, days: {}".format(transaction, day)
	if not len(stack):
		print "No transactions!"
	else:
		for entry in range(len(stack)-1, -1, -2):
			print "Buy on day {day}, at price {price}".format(day=stack[entry], price=stock[stack[entry]])
			print "Sell on day {day}, at price {price}".format(day=stack[entry-1], price=stock[stack[entry-1]])

if __name__ == '__main__':
	# stock = [10, 22, 5, 75, 65, 80]
	# k = 2

	# stock = [90, 80, 70, 60, 50]
	# k = 1

	stock = [100, 30, 15, 10, 8, 25, 80]
	k = 3

	# stock = [12, 14, 17, 10, 14, 13, 12, 15]
	# k = 3
	print maxProfitEfficient(stock, k)
