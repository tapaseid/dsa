# Count of different ways to express N as the sum of 1, 3 and 4

# Base cases: d[0] = 1, d[1] = 1, d[2] = 1, d[3] = 2
# Recurrence relation: d[n] = d[n-1] + d[n-3] + d[n-4]

def count_ways(n):
	d = [0]*(n+1)

	d[0] = d[1] = d[2] = 1
	d[3] = 2

	for i in range(4, n+1):
		d[i] = d[i-1] + d[i-3] + d[i-4]

	return d[n]

if __name__ == '__main__':
	print count_ways(10)
