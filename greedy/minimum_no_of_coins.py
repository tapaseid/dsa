# Coin change problem.
# This is not perfect implementation, should solve using dp.

DENO = [1, 2, 5, 10, 20, 50, 100, 500, 1000, 2000]

def minCoinRequired(value):
	n = len(DENO)
	ans_stack = []
	for i in range(n-1, -1, -1):
		while value >= DENO[i]:
			value -= DENO[i]
			ans_stack.append(DENO[i])
	return ans_stack

if __name__ == '__main__':
	value = 159
	print minCoinRequired(value)
