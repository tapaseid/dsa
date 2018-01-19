# Celebrity problem.
# In a party of N people, only one person is known to everyone. 
# Such a person may be present in the party, if yes, (s)he does not know anyone in the party. 
# We can only ask questions like "does A know B?". 
# Find the stranger (celebrity) in minimum number of questions.

def findCelebrity(c_m, n):
	if n < 2:
		return -1

	stack = [i for i in range(n)]
	a = stack[-1]
	b = stack[-2]

	while len(stack) > 1:
		a = stack.pop()
		b = stack.pop()
		# print "A:{}, B:{}".format(a, b)
		if c_m[a][b]:
			stack.append(b)
		else:
			stack.append(a)

	c = stack.pop()

	# Last candidate was not examined, it leads one excess comparison (optimize)
	if c_m[c][b]:
		c = b
	if c_m[c][a]:
		c = a

	# Check if C is actually a celebrity or not
	for i in range(n):
		# If any person doesn't know 'c' or 'c' doesn't know any person, return -1
		if i != c and (c_m[c][i] or not c_m[i][c]):
			return -1

	return c

if __name__ == '__main__':
	celebrity_matrix = [[0, 0, 1, 0],
						[0, 0, 1, 0],
						[0, 0, 0, 0],
						[0, 0, 1, 0]
					   ]
	n = len(celebrity_matrix)
	print "Celebrity ID:", findCelebrity(celebrity_matrix, n)