# Pattern searching is an important problem in computer science.
# When we do search for a string in notepad/word file or browser or database,
# pattern searching algorithms are used to show the search results.

# We'll propose different algos to improve time complexity!


def Naive_pattern_searching(pat, txt):
	# Time complexity = O(m*(n-m+1))

	M = len(pat)
	N = len(txt)

	for i in range(N-M+1):
		for j in range(M):
			if pat[j] != txt[i+j]:
				break
		if j == M-1:
			print "Pattern found at index:", i
		elif j == 0:
			i += 1
		else:
			i += j

def KMP_algo(pat, txt):
	# KMP (Knuth Morris Pratt) Pattern Searching
	# Time complexity = O(n)

	M = len(pat)
	N = len(txt)

	lps = [0]*M
	computeLPSArray(pat, lps, M)

	i = j = 0
	while i < N:
		if pat[j] == txt[i]:
			i += 1
			j += 1
		if j == M:
			print "Pattern found at index:", i-j
			j = lps[j-1]

		elif i < N and pat[j] != txt[i]:
			if j != 0:
				j = lps[j-1]
			else:
				i += 1

def computeLPSArray(pat, lps, M):
	j = 0
	lps[0] = j
	i = 1
	while i < M:
		if pat[i] == pat[j]:
			j += 1
			lps[i] = j
			i += 1
		else:
			if j != 0:
				j = lps[j-1]
			else:
				lps[i] = 0
				i += 1
	# print "LPS:", lps

d = 256
def Rabin_Karp_algo(pat, txt, q):
	# Time complexity O(m*(n-m+1))
	# But couple of advantages than Naive algo

	M = len(pat)
	N = len(txt)
	i = j = 0
	p = t = 0 # hash values for pattern and txt resp.
	h = 1

	for i in range(M-1):
		h = (h*d)%q
	# print "H:", h
	for i in range(M):
		p = (d*p + ord(pat[i]))%q
		t = (d*t + ord(txt[i]))%q

	for i in range(N-M+1):
		if p == t:
			for j in range(M):
				if pat[j] != txt[i+j]:
					break
			if j == M-1:
				print "patter found at index:", i
		if i < N-M:
			t = (d*(t - ord(txt[i])*h) + ord(txt[i+M]))%q
			if t < 0:
				t = t + q


NO_OF_CHARS	= 256
def getNextState(pat, M, state, x):
	if state < M and x == ord(pat[state]):
		return state+1

	i = 0
	for ns in range(state, 0, -1):
		if ord(pat[ns-1]) == x:
			while i < ns-1:
				if pat[i] != pat[state-ns+1+i]:
					break
				i += 1
			if i == ns-1:
				return ns
	return 0

def computeTF(pat, M):
	# Time complexity to construct TF O(m^3*NO_OF_CHARS)

	TF = [[0 for i in range(NO_OF_CHARS)] for j in range(M+1)]
	for state in range(M+1):
		for x in range(NO_OF_CHARS):
			z = getNextState(pat, M, state, x)
			TF[state][x] = z

	return TF

def computeTransFunEfficient(pat, M):
	# Time complexity to construct TF O(m*NO_OF_CHARS)

	TF = [[None for i in range(NO_OF_CHARS)] for _ in range(M+1)]
	for i in range(NO_OF_CHARS):
		TF[0][i] = 0
	TF[0][ord(pat[0])] = 1

	lps = 0
	for i in range(1, M+1):
		for j in range(NO_OF_CHARS):
			TF[i][j] = TF[lps][j]
		
		if i < M:
			TF[i][ord(pat[i])] = i+1
			lps = TF[lps][ord(pat[i])]

	return TF

def Finite_Automata(pat, txt):
	# time complexity for searching O(n)

	M = len(pat)
	N = len(txt)
	TF = computeTransFunEfficient(pat, M)

	state = 0
	for i in range(N):
		state = TF[state][ord(txt[i])]
		if state == M:
			print "Pattern found at index:{}".format(i-M+1)


# Driver program
if __name__ == '__main__':
	txt = "AABAABAAAAAABABAABAAABA"
	pat = "AABA"
	Naive_pattern_searching(pat, txt)
	# KMP_algo(pat, txt)

	# q = 101
	# Rabin_Karp_algo(pat, txt, q)

	Finite_Automata(pat, txt)

