# Given a binary string, find largest length of equal no of 0s and 1s

def fing_substring_length(s, n):
	m = dict()
	m[0] = -1

	count_0 = 0
	count_1 = 0
	res = 0

	for i in range(n):
		if s[i] == '0':
			count_0 += 1
		if s[i] == '1':
			count_1 += 1

		if m.get(count_1 - count_0):
			res = max(res, i - m[count_1 - count_0])
		else:
			m[count_1 - count_0] = i

	return res

def max_consecutive_1(input_str):

	# return max(map(len, input_str.split('0')))

	count = 0
	res = 0

	for i in range(len(input_str)):
		if input_str[i] == '0':
			count = 0
		else:
			count += 1
			res = max(res, count)

	return res

if __name__ == '__main__':
	# s = "11010111"
	s = '1100000000111'
	print fing_substring_length(s, len(s))

	input_str = '11000111101010111'
	print max_consecutive_1(input_str)
