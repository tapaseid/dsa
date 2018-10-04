# Find pairs from two lists such that swapping the value of each pair 
# makes two lists as equal sum


# Return l1 as bigger sum, l2 as smaller sum, difference of l1 and l2
# and flag(to determine in which order pair should store vaules)
def check_bigger_sum_and_diff(l1, l2):
	if sum(l1) > sum(l2):
		return l1, l2, sum(l1) - sum(l2), True
	else:
		return l2, l1, sum(l2) - sum(l1), False

def get_pairs(l1, l2):
	l1 = sorted(l1)
	l2 = sorted(l2)

	l1, l2, diff, flag = check_bigger_sum_and_diff(l1, l2)

	if diff&1:
		print "Pairs not possible!"
		return
	
	pairs = []
	i, j = 0, 0
	while i < len(l1) and j < len(l2):
		d = l1[i] - l2[j]
		if d < diff/2:
			i += 1
		elif d > diff/2:
			j += 1
		else:
			if flag:
				pairs.append((l1[i], l2[j]))
			else:
				pairs.append((l2[j], l1[i]))
			i += 1
			j += 1
	return pairs


# l1 = [1, 2, 3, 4, 8]
# l2 = [1, 2, 3, 4, 4]

# l1 = [2, 3, 6]
# l2 = [1, 3, 5, 8]

l1 = [2, 6, 3]
l2 = [3, 1, 8, 5]

pairs = get_pairs(l1, l2)
if pairs:
	for i in pairs:
		print i
 
