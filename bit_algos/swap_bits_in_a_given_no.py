# Given a number x and two positions (from right side) in binary
# representation of x, write a function that swaps n bits at given
# two positions and returns the result. It is also given that
# the two sets of bits do not overlap.

# Example
# Input:
# x = 28 (11100)
# p1 = 0 (Start from first bit from right side)
# p2 = 3 (Start from 4th bit from right side)
# n = 2 (No of bits to be swapped)
# Output:
# 7 (00111)
# The 2 bits starting from 0th postion (from right side) are
# swapped with 2 bits starting from 4th position (from right side)

def swapBits(given_no, p1, p2, n):
	
	# move all bits of first set to rightmost side
	set1 = (given_no>>p1)&((1<<n)-1)

	# move all bits of second set to rightmost side
	set2 = (given_no>>p2)&((1<<n)-1)

	# XOR the two sets
	xor = set1^set2

	# put the xor bits back to their original positions
	xor = (xor<<p1) | (xor<<p2)

	# XOR the 'xor' wirh original number so that the two sets are swapped
	result = given_no^xor
	return result

if __name__ == '__main__':
	print swapBits(28, 0, 3, 2)
