# To find the element that appears once.


# This method is for an array where every element occurs three times,
# except one element which occurs only once.
def getSingle(lst):
	# Time complexity O(n)
	# Space complexity O(1)
	ones = 0
	twos = 0
	for i in range(len(lst)):
		twos |= ones&lst[i]
		ones ^= lst[i]
		common_bit_mask = ~(ones&twos)
		# print common_bit_mask
		ones &= common_bit_mask
		twos &= common_bit_mask
	return ones

def getSingle_another(lst):
	# Time complexity O(n)

	return (3*sum(set(lst))-sum(lst))/2

if __name__ == '__main__':
	lst = [3, 3, 2, 3, 1, 1, 1]

	print "Single element is", getSingle(lst)
	print "Single element is", getSingle_another(lst)
