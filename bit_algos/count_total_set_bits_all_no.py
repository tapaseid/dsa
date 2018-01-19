# Given a positive integer n, count the total number of set bits in
# binary representation of all numbers from 1 to n.

def count_set_bits(n):
	# Time complexity O(nLog n)

	bitCount = 0
	for i in range(1, n+1):
		bitCount += count_set_bits_Util(i)

	return bitCount

def count_set_bits_Util(x):
	if x <=0:
		return 0

	if x%2 == 0:
		return 0 + count_set_bits_Util(x/2)
	else:
		return 1 + count_set_bits_Util(x/2)



# Another efficient method!
def getLeftMostBit(n):
	m = 0
	while n>1:
		n = n >> 1
		m += 1
	return m

def getNextLeftMostBit(n, m):
	temp = 1 << m
	while n < temp:
		temp = temp >> 1
		m -= 1
	return m

def _countSetBits(n, m):
	if n == 0:
		return 0

	m = getNextLeftMostBit(n, m)
	if n == (1<<(m+1)) - 1:
		return (m+1)*(1<<m)

	n = n - (1<<m)
	return (n+1) + countSetBits(n) + m*(1<<(m-1))

def countSetBits(n):
	# Time complexity O(log n)

	m = getLeftMostBit(n)
	return _countSetBits(n, m)

def main():
	print count_set_bits(4)
	print "Other method:", countSetBits(4)

if __name__ == '__main__':
	main()
