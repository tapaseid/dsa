# Given a string, find the longest substring which is palindrome.

# Time complexity ---> O(n*n)
# Space complexity ---> O(n*n)
def longest_palindromic_substring(s):
	n = len(s)

	start = 0
	max_length = 1
	t = [[None]*n for _ in range(n)]
	for i in range(n):
		t[i][i] = True

	for i in range(n-1):
		if s[i] == s[i+1]:
			t[i][i+1] = True
			start = i
			max_length = 2

	for l in range(3, n):
		for i in range(n-l+1):
			j = i+l-1
			if s[i] == s[j] and t[i+1][j-1]==True:
				t[i][j] = True
				start = i
				max_length = l
			else:
				t[i][j] == False

	return s[start:start+max_length]


# Time complexity ---> O(n*n)
# Space complexity ---> O(1)
def longest_palindromic_substring_efficient(s):
	n = len(s)
	start = 0
	max_length = 1

	for i in range(1, n):
		low = i-1
		high = i

		while low >= 0 and high < n and s[low]==s[high]:
			if high-low > max_length:
				start = low
				max_length = high-low
			low -= 1
			high += 1

		low = i-1
		high = i+1

		while low >= 0 and high < n and s[low]==s[high]:
			if high-low > max_length:
				start = low
				max_length = high-low
			low -= 1
			high += 1

	return s[start:start+max_length+1]


# Time complexity ---> O(n)
def Manachers_algo(s):
	n = len(s)
	if n == 0:
		return
	n = 2*n + 1
	l = [0]*n
	l[0], l[1] = 0, 1

	c = 1 # centerPosition
	r = 2 # centerRightPossition
	i = 0 # currentRightPossition

	iMirror = 0 # currentLeftPosition
	maxLPSLength = 0
	maxLPSCenterPosition = 0
	start = -1
	end = -1
	diff = -1

	for i in range(2, n):
		iMirror = 2*c -1
		l[i] = 0
		diff = r - i
		if diff>0:
			l[i] = min(l[iMirror], diff)

		try:
			while i+l[i] < n and i-l[i] > 0 and((i+l[i]+1)%2==0 or \
				s[(i+l[i]+1)/2]==s[(i-l[i]-1)/2]):
				l[i] += 1
		except Exception as e:
			pass

		if l[i] > maxLPSLength:
			maxLPSLength = l[i]
			maxLPSCenterPosition = i

		if i + l[i] > r:
			c = i
			r = i + l[i]

	start = (maxLPSCenterPosition - maxLPSLength)/2
	end = start + maxLPSLength -1
	return s[start:end+1] 

def test(s):
	n = len(s)
	l = ''

	for i in range(n):
		if i&1:
			left, right = i/2, i/2+1
		else:
			left, right = i/2-1, i/2+1
		while left >= 0 and right < n and s[left] == s[right]:
			left -= 1
			right += 1
		if right - left -1 > len(l):
			l = s[left+1:right]

	return l


if __name__ == '__main__':
	s = "forgeeksskeegfor"
	# s = 'bananas'
	print test(s)
	print longest_palindromic_substring(s)
	print longest_palindromic_substring_efficient(s)
	print Manachers_algo(s)
