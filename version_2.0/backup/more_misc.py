import sys, os

def is_feasible(arr, mid, n, k):
	pos = arr[0]
	count = 1

	for i in range(1, n):
		if arr[i] - pos >= mid:
			count += 1
			pos = arr[i]

			if count == k:
				return True
	return False


# Ex - aggressive cows

def place_k_element_with_largest_min_distance(arr, k):
	arr.sort()
	n = len(arr)
	res = -1
	
	left = arr[0]
	right = arr[n-1]

	while left < right:
		mid = int((left+right)/2)

		if is_feasible(arr, mid, n, k):
			res = max(res, mid)
			left = mid + 1
		else:
			right = mid

	return res

arr = [6, 9, 7, 21, 13]
# arr = [1, 2, 8, 4, 9]
k = 3
# print(place_k_element_with_largest_min_distance(arr, k))



def root(x, n):
  e = 0.001
  left, right = 0, max(1, x)
  while right - left > e:
		mid = float(left + right)/2
		tmp = mid
		for i in range(1, n):
		  tmp *= mid
		if tmp == x:
		  return round(mid, 3)
		elif tmp > x:
		  right = mid
		else:
		  left = mid
	  
  return round(mid, 3)

# print root(7, 3)



def mySqrt(x):
        if x < 2:
            return x
        
        left, right = 1, x
        while left < right:
            mid = (left + right)/2
            print "MID: ", mid, left, right
            if mid*mid == x:
              return mid
            elif mid*mid < x:
              left = mid+1
              ans = mid
            else:
              right = mid

        return ans

# print mySqrt(8)


def custom_pow(x, y):
    res = 1
    while y>0:
        if y&1:
            res *= x
        y >>= 1
        x *= x
    return res
# print custom_pow(2, 3)


from heapq import heapify, heappush, heappop
def sort_k_messed_array(arr, k):
  h = arr[:k+1]
  heapify(h)
  idx = 0
  for i in range(k + 1, len(arr)):
    arr[idx] = heappop(h)
    idx += 1
    heappush(h,arr[i])
    
  while h:
    arr[idx] = heappop(h)
    idx += 1
  return arr

arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
k = 2
# sort_k_messed_array(arr, k)
# print arr


# Alien dictionary
'''
There is a new alien language that uses the English alphabet.
However, the order among the letters is unknown to you.
You are given a list of strings words from the alien language's dictionary, 
where the strings in words are sorted lexicographically by the rules of this new language.
Return a string of the unique letters in the new alien language sorted in lexicographically 
increasing order by the new language's rules. If there is no solution, return "". 
If there are multiple solutions, return any of them.

A string s is lexicographically smaller than a string t if at the first letter where they differ, 
the letter in s comes before the letter in t in the alien language. If the first min(s.length, t.length) 
letters are the same, then s is smaller if and only if s.length < t.length.

 
Example 1:
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Example 2:
Input: words = ["z","x"]
Output: "zx"

Example 3:
Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".

'''

def alienOrder(words):
	adj = {c: set() for w in words for c in w}
	for i in range(len(words) - 1):
		w1, w2 = words[i], words[i+1]
		min_len = min(len(w1), len(w2))

		if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
			return ""
		for j in range(min_len):
			if w1[j] != w2[j]:
				adj[w1[j]].add(w2[j])
				break

	# print adj

	seen = {}  # True->seen(grey), False->dead(in the current path)
	result = []

	def dfs(c):
		if c in seen:
			return seen[c]

		seen[c] = True
		for nei in adj[c]:
			if dfs(nei):
				return True

		seen[c] = False
		result.append(c)

	for c in adj:
		if dfs(c):
			return ""

	result.reverse()
	return ''.join(result)



words = ["wrt","wrf","er","ett","rftt"]
# words = ["z","x","z"]
# print alienOrder(words)



# Longest palindromic substring - Manachers algo
def UpdatedString(string):
    newString = ['#']
    for char in string:
        newString += [char, '#']
    return ''.join(newString)

def Manachen(string):
    string = UpdatedString(string)
    LPS = [0 for _ in range(len(string))]
    C = 0
    R = 0

    for i in range(len(string)):
        iMirror = 2*C - i
        if R > i:
            LPS[i] = min(R-i, LPS[iMirror])
        else:
            LPS[i] = 0
        try:
            while string[i + 1 + LPS[i]] == string[i - 1 - LPS[i]]:
                LPS[i] += 1
        except:
            pass
        
        if i + LPS[i] > R:
            C = i
            R = i + LPS[i]
    
    r, c = max(LPS), LPS.index(max(LPS))
    print (string[c - r : c + r].replace("#",""))
    return r

# print(Manachen("acaac"))



'''
input:  document = "Practice makes perfect. you'll only
                    get Perfect by practice. just practice!"

output: [ ["practice", "3"], ["perfect", "2"],
          ["makes", "1"], ["youll", "1"], ["only", "1"], 
          ["get", "1"], ["by", "1"], ["just", "1"] ]
'''


from collections import defaultdict
def word_count_engine(document):
  lst = document.split()
  dct = defaultdict(int)
  max_freq = 0
  for i in range(len(lst)):
    word = lst[i].lower()
    clean_word = []
    for ch in word:
      if ch >= 'a' and ch <= 'z':
      	clean_word.append(ch)

    lst[i] = ''.join(clean_word)
    dct[lst[i]] += 1
    max_freq = max(max_freq, dct[lst[i]])
  
  # print dct
  # dct = sorted(dct, key=lambda x: dct[x], reverse = True)
  # print dct
  tmp = [[] for i in range(max_freq+1)]
  for word in lst:
  	if dct.get(word):
  		tmp[dct.get(word)].append(word)
  		del dct[word]
  res = []
  for i in range(max_freq, 0, -1):
  	for word in tmp[i]:
  		res.append([word, str(i)])
  
  return res

document = "youll Practice makes perfect. you'll only get Perfect by practice. just practice!"
print word_count_engine(document)




## Remove Invalid Parentheses
# Input  : str = "()())()" -
# Output : ()()() (())()
# There are two possible solutions
# "()()()" and "(())()"

# Input  : str = (v)())()
# Output : (v)()()  (v())()

def isValid(tmp):
    count = 0

    for ch in tmp:
        if ch == '(':
            count += 1
        elif ch == ')':
            count -= 1
            if count < 0:
                return False

    return count == 0

def remove_invalid_parenthesis(s):
    res = []
    if not len(s):
        return res

    level = False
    q = [s]
    seen = set(s)
    while q:
        tmp = q.pop(0)
        
        if isValid(tmp):
            res.append(tmp)
            level = True

        if level:
            continue

        for i in range(len(tmp)):
            new_str = tmp[:i] + tmp[i+1:]
            if new_str not in seen:
                q.append(new_str)
                seen.add(new_str)
    return res


expression = '()())()'
# expression = "()v)"
# print remove_invalid_parenthesis(expression)




# Minimum Swaps required to group all 1's together
# Given an array of 0's and 1's, we need to write a program to find the 
# minimum number of swaps required to group all 1's present in the array together.
# Input : arr[] = {1, 0, 1, 0, 1}
# Output : 1
# Explanation: Only 1 swap is required to group all 1's together.
# Swapping index 1 and 4 will give arr[] = {1, 1, 1, 0, 0}

# Input : arr[] = {1, 0, 1, 0, 1, 1}
# Output : 1

def min_swap_required(arr):
    size_window = sum(arr)
    window_count = sum(arr[:size_window])
    res = size_window - window_count

    j = size_window

    while j < len(arr):
        if arr[j]:
            window_count += 1

        if arr[j - size_window]:
            window_count -= 1

        res = min(res, size_window - window_count)
        j += 1

    return res

# arr = [1, 0, 1, 0, 1] # ans = 1
# arr = [0, 0, 0, 1, 0] # ans = 0
arr = [1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1] # ans = 3
# print min_swap_required(arr)



# # Find the longest substring with k unique characters in a given string
# "aabbcc", k = 1
# Max substring can be any one from {"aa" , "bb" , "cc"}.

# "aabbcc", k = 2
# Max substring can be any one from {"aabb" , "bbcc"}.

# "aabbcc", k = 3
# There are substrings with exactly 3 unique characters
# {"aabbcc" , "abbcc" , "aabbc" , "abbc" }
# Max is "aabbcc" with length 6.

# "aaabbb", k = 3
# There are only two unique characters, thus show error message.

def longest_substring_with_at_most_k_distinct_chars(s, k):
    mp = dict()
    start, end = 0, 0
    res = -1
    while end < len(s):
        mp[s[end]] = mp.get(s[end], 0) + 1
        if len(mp) == k:
            res = max(res, end-start+1)

        while len(mp) > k:
            mp[s[start]] -= 1
            if mp[s[start]] == 0:
                del mp[s[start]]
            start += 1
        end += 1
    
    return res


s, k = "aabbcc", 2
# print longest_substring_with_at_most_k_distinct_chars(s, k)


## Find the valid sentense using word dictionary provided.
def valid_sentense(s, word_dict):
    q = [(0, '')]
    visited = set()
    while q:
        start, tmp = q.pop(0)
        if start in visited:
            continue
        visited.add(start)
        for end in range(start + 1, len(s) + 1):
            curr_word = s[start: end]
            if curr_word in word_dict:
                q.append((end, tmp + ' ' + curr_word if tmp else curr_word))
                if end == len(s):
                    return tmp + ' ' + curr_word if tmp else curr_word
    return ''

# s = 'iamtapas'
# s = 'heshehe'
s = 'heistheking'
# s = 'shehe'
# s = 'catsanddog'
word_dict = ['i', 'am', 'tapas', 'he', 'she', 'the', 'king', 'is', 'cat', 'dog', 'sand', 'cats', 'and']
# print valid_sentense(s, word_dict)


### LC 140. Word Break II
# Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

# Example 1:

# Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
# Output: ["cats and dog","cat sand dog"]
# Example 2:

# Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
# Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
# Explanation: Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: []

### JAVA working solution
# class Solution {
#     public List<String> wordBreak(String s, List<String> wordDict) {
#         Map<String, List<String>> map = new HashMap<>();
#         return helper(s, wordDict, map);
#     }
    
#     private List<String> helper(String s, List<String> wordDict, Map<String, List<String>> map) {
        
#         if(map.containsKey(s)) {
#             return map.get(s);
#         }
        
#         List<String> temp = new ArrayList<>();
#         for(String word: wordDict) {
#             if(s.startsWith(word)) {
#                 if(s.length() == word.length()) {
#                     temp.add(word);
#                 }
#                 else {
#                     List<String> combinations = helper(s.substring(word.length()), wordDict, map);
                    
#                     for(String combination: combinations) {
#                         // System.out.println(combination);
#                         temp.add(word + " " +combination);
#                     }
#                 }
                
#             }

#         }
        
#         map.put(s, temp);
#         return map.get(s);
        
#     }
# }




# class Solution(object):
# def wordBreak(self, s, wordDict):
#     """
#     :type s: str
#     :type wordDict: Set[str]
#     :rtype: List[str]
#     """
#     return self.helper(s, wordDict, {})
    
# def helper(self, s, wordDict, memo):
#     if s in memo: return memo[s]
#     if not s: return []
    
#     res = []
#     for word in wordDict:
#         if not s.startswith(word):
#             continue
#         if len(word) == len(s):
#             res.append(word)
#         else:
#             resultOfTheRest = self.helper(s[len(word):], wordDict, memo)
#             for item in resultOfTheRest:
#                 item = word + ' ' + item
#                 res.append(item)
#     memo[s] = res
#     return res



