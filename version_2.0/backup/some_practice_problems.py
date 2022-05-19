
import sys, os

# https://www.scaler.com/academy/mentee-dashboard/classroom/searching-i-4cedf614-ad49-42ee-ac8b-32d95b81a7af/#lecture

# 1. partition painter
# 2. Aggressive Cow


# 4 7 3 1 9 10 -> caves
# 3 1 5 9 8 ->statues


## Ways to arrange Balls such that adjacent balls are of different types
# https://www.geeksforgeeks.org/ways-to-arrange-balls-such-that-adjacent-balls-are-of-different-types/
# Input  : p = 1, q = 1, r = 0
# Output : 2
# There are only two arrangements PQ and QP

# Input  : p = 1, q = 1, r = 1
# Output : 6
# There are only six arrangements PQR, QPR,
# QRP, RQP, PRQ and RPQ

# Input  : p = 2, q = 1, r = 1
# Output : 6
# There are only six arrangements PQRP, QPRP,
# PRQP, RPQP, PRPQ and PQPR

def count_ways_helper(p, q, r, last):
    if p < 0 or q < 0 or r < 0:
        return 0
    if p == 1 and q == 0 and r == 0 and last == 0:
        return 1
    if p == 0 and q == 1 and r == 0 and last == 1:
        return 1
    if p == 0 and q == 0 and r == 1 and last == 2:
        return 1

    if last == 0:
        return count_ways_helper(p-1, q, r, 1) + count_ways_helper(p-1, q, r, 2)
    if last == 1:
        return count_ways_helper(p, q-1, r, 0) + count_ways_helper(p, q-1, r, 2)
    if last == 2:
        return count_ways_helper(p, q, r-1, 0) + count_ways_helper(p, q, r-1, 1)

def count_ways(p, q, r):
    # return count_ways_helper(p, q, r, 0) + count_ways_helper(p, q, r, 1) + count_ways_helper(p, q, r, 2)
    

    def count_ways_dp(p, q, r, last):
        if p < 0 or q < 0 or r < 0:
            return 0
        if p == 1 and q == 0 and r == 0 and last == 0:
            return 1
        if p == 0 and q == 1 and r == 0 and last == 1:
            return 1
        if p == 0 and q == 0 and r == 1 and last == 2:
            return 1

        if dp[p][q][r][last] != -1:
            return dp[p][q][r][last]

        if last == 0:
            dp[p][q][r][last] = count_ways_dp(p-1, q, r, 1) + count_ways_dp(p-1, q, r, 2)
        elif last == 1:
            dp[p][q][r][last] = count_ways_dp(p, q-1, r, 0) + count_ways_dp(p, q-1, r, 2)
        else: #if last == 2:
            dp[p][q][r][last] = count_ways_dp(p, q, r-1, 0) + count_ways_dp(p, q, r-1, 1)

        return dp[p][q][r][last]

    # assuming the value of p, q, r not more than 99
    dp = [[[[-1]*4 for i in range(100)] for j in range(100)] for k in range(100)]
    return count_ways_dp(p, q, r, 0) + count_ways_dp(p, q, r, 1) + count_ways_dp(p, q, r, 2)

p, q, r = 2, 1, 1
print count_ways(p, q, r)

# Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.
# If there is no non-empty subarray with sum at least K, return -1.
# Example 1: Input: A = [1], K = 1
#            Output: 1
# Example 2: Input: A = [1,2], K = 4
#            Output: -1
# Example 3: Input: A = [2,-1,2], K = 3
#            Output: 3

def smallest_window_sum_atleast_k(arr, k):
    n = len(arr)
    min_len = float('inf')

    q = [(-1, 0)]
    prefix_sum = 0
    for i in range(n):
        prefix_sum += arr[i]
        while q and prefix_sum - q[0][1] >= k:
            min_len = min(min_len, i-q[0][0])
            q.pop(0)
        while q and q[-1][1] > prefix_sum:
            q.pop()
        q.append((i, prefix_sum))
    return min_len if min_len != float('inf') else -1


class Solution(object):
    def shortestSubarray(self, A, K):
        N = len(A)
        P = [0]
        for x in A:
            P.append(P[-1] + x)

        #Want smallest y-x with Py - Px >= K
        ans = N+1 # N+1 is impossible
        monoq = collections.deque() #opt(y) candidates, represented as indices of P
        for y, Py in enumerate(P):
            #Want opt(y) = largest x with Px <= Py - K
            while monoq and Py <= P[monoq[-1]]:
                monoq.pop()

            while monoq and Py - P[monoq[0]] >= K:
                ans = min(ans, y - monoq.popleft())

            monoq.append(y)

        return ans if ans < N+1 else -1


arr = [2, -1, 2, 1]
k = 3
# print smallest_window_sum_atleast_k(arr, k)



def equilibrium_point(arr):
    res = []
    cum_sum = 0
    for i in range(len(arr)):
        cum_sum += arr[i]
    left_sum = 0
    for i in range(len(arr)):
        right_sum = cum_sum - left_sum - arr[i]
        if right_sum == left_sum:
            res.append(i)
        left_sum += arr[i]

    return res

arr = [0, -3, 5, -4, -2, 3, 1, 0]
# print equilibrium_point(arr)


# Problem: Regular expression match - https://leetcode.com/problems/regular-expression-matching/
# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

'''
dp[i][j] = dp[i-1][j-1] if string[i] == pattern[j] or pattern[j] == '.' 
         = dp[i][j-2] if 0 occurrence, i.e pattern[j] == '*'
         = dp[i][j] or dp[i-1][j] --- if pattern[j] == '*' and (if string[i] == pattern[j-1] or pattern[j-1] == '.')
'''
def regx_match(pattern, string):
    m = len(string)
    n = len(pattern)

    dp = [[None]*(n+1) for _ in range(m+1)]

    dp[0][0] = True

    for i in range(1, m+1):
        dp[i][0] = False
    for j in range(1, n+1):
        if pattern[j-1] == '*':
            dp[0][j] == dp[0][j-2]
        else:
            dp[0][j] = False

    for i in range(1, m+1):
        for j in range(1, n+1):
            if string[i-1] == pattern[j-1] or pattern[j-1] == '.':
                dp[i][j] = dp[i-1][j-1]
            elif pattern[j-1] == '*':
                dp[i][j] = dp[i][j-2]
                if string[i-1] == pattern[j-2] or pattern[j-2] == '.':
                    dp[i][j] = dp[i][j] or dp[i-1][j]
            else:
                dp[i][j] = False
    
    # for i in range(m+1):
    #     print dp[i]
    return dp[-1][-1]


pattern = 'xa*b.c'
string = 'xaabyc'

# print regx_match(pattern, string)

def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    # if not p:
    #     return not s
    # first_match = bool(s) and p[0] in {s[0], '.'}
    # if len(p) >= 2 and p[1] == '*':
    #     return (isMatch(s, p[2:]) or first_match and isMatch(s[1:], p))
    # else:
    #     return first_match and isMatch(s[1:], p[1:])
    
    
    dp = [[False]*(len(p) + 1) for _ in range(len(s) + 1)]
    
    dp[-1][-1] = True
    for i in range(len(s), -1, -1):
        for j in range(len(p)-1, -1, -1):
            first_match = i < len(s) and p[j] in {s[i], '.'}
            if j+1 < len(p) and p[j+1] == '*':
                dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
            else:
                dp[i][j] = first_match and dp[i+1][j+1]
    return dp[0][0]



## Wildcard pattern matching  - https://leetcode.com/problems/wildcard-matching/
# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).

def is_match(s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False]*(len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        
        # if len(p) > 0 and p[0] == '*':
        #     dp[0][1] = True
        # for j in range(2, len(p) + 1):
        #     if p[j-1] == '*' and dp[0][j-1]:
        #         dp[0][j] = True
        
        for j in range(1, len(p) + 1):
            if p[j-1] != '*':
                break
            dp[0][j] = True
        
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j] # dp[i][j-1] or dp[i-1][j] or dp[i-1][j-1]
                if p[j-1] in {s[i-1], '?'}:
                    dp[i][j] = dp[i-1][j-1]
        
        return dp[-1][-1]

s, p = 'cat', 'c*t'
# s, p = '', '*'
# print is_match(s, p)


# house and energy
# there are n houses with some initial energy
# in each house you can either steal the coin or you can recharge from it 
# while moving to the next house you spend 1 unnit of energy
# you have to pick maximum number of coins
# energy =   5  1  1
# coins =    5 100 7
# 1000
# dp[i][j] = sufix of i with energy j when i starts from i
# if(j>1000)
# return coinsum[];
# else if(j==0){
#     max(coin[i],dp[i+1][min(1000,j+energy[i]-1)]);
# }


# fun(arr, k, curr_index)
#     if k == 0
#        return True
#     if len(arr) == 0 or curr_index >= len(arr):
#         False
        
#     if arr[curr_index] < k:
#         return fun(arr, k - arr[curr_index], curr+index + 1)
#     return fun(arr, k, curr+index + 1)

# def is_subset_sum(arr, k):
#     n = len(arr)
#     dp [[False]*(k+1) for _ in range(n)]]
#     for i in range(n):
#         dp[i][0] = True
    
#     for j in range(1, k+1):
#         if arr[0] == k:
#             dp[0][j] = True
    
#     for i in range(1, n):
#         for j in range(1, k+1):
#             if dp[i-1][j]:
#                 dp[j][j] = True
#             else:
#                 if dp[i-1][j]:
#                     dp[i][j] = dp[i-1][j]
#                 elif j <= arr[i]:
#                     dp[i][j] = dp[i-1][j-arr[i]]
     
#     return dp[n-1][k] 


# https://www.scaler.com/academy/mentee-dashboard/classroom/designing-the-pathway-to-success-48083be1-573d-4700-bc26-5c02db7fdb0f/#lecture
# Problem: Stock buy and sell K transaction
# #########################################
def stock_buy_sell(stock, k):
    n = len(stock)

    dp = [[0]*n for _ in range(k+1)]

    for i in range(1, k+1):
        max_diff = -sys.maxint
        for j in range(1, n):
            max_diff = max(max_diff, dp[i-1][j-1]-stock[j-1])
            dp[i][j] = max(dp[i][j-1], stock[j]+max_diff)

    # for i in range(k+1):
    #     print dp[i]

    return dp[-1][-1]


stock = [2, 4, 5, 3, 9]

# print stock_buy_sell(stock, 2)


# Palindrome partition

def palindrome_partition(s):
    n = len(s)

    dp = [[None]*n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 0

    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i+l-1
            if s[i] == s[j]:
                dp[i][j] = 0
            else:
                min_val = n
                for k in range(i, j):
                    min_val = min(min_val, dp[i][k]+dp[k+1][j])
                    dp[i][j] = 1 + min_val
    
    # for i in range(n):
    #     print dp[i]

    return dp[0][-1]

s = 'abcbm'
# print palindrome_partition(s)



# Word search/suggestion

# Problem: Trie
# #############


class TrieNode:
    def __init__(self, ch=None):
        self.ch = ch
        self.children = [None]*26
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, string):
        current_node = self.root
        length = len(string)
        for i in range(length):
            ch = string[i]
            index = ord(ch)-ord('a')

            if current_node.children[index] is None:
                current_node.children[index] = TrieNode(ch)
            
            current_node = current_node.children[index]
        current_node.isEndOfWord = True

    def search(self, string):
        current_node = self.root

        length = len(string)
        for i in range(length):
            ch = string[i]
            index = ord(ch)-ord('a')
            if current_node.children[index] is None:
                return False
            current_node = current_node.children[index]

        if current_node.isEndOfWord:
            return True
        return False

    def isValidWord(self, string):
        current_node = self.root

        length = len(string)
        for i in range(length):
            ch = string[i]
            index = ord(ch)-ord('a')
            if current_node.children[index] is None:
                return False
            current_node = current_node.children[index]
        return True


words = ["cat", "cats", "dog", "and", "dogs", "hello"]

obj = Trie()

for s in words:
    obj.insert(s)

# print obj.search("dogsu")

st = "dowgds"
res = ''
ans = set()
for i in range(len(st)):
    ch = st[i]
    res += ch
    if not obj.isValidWord(res):
        res = res[:-1]
    if obj.search(res):
        ans.add(res)

    
# word break
def check_word_break(stt, root):
    n = len(stt)
    if n == 0:
        return True

    for i in range(1, n+1):
        if root.search(stt[:i]) and check_word_break(stt[i:], root):
            return True
    return False

def word_break_dp(s, root):
    n = len(s)

    dp = [[False]*n for _ in range(n)]

    for i in range(n):
        if root.search(s[i:i+1]):
            dp[i][i] = True

    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i+l-1
            if root.search(s[i:i+l]):
                dp[i][j] = True
            else:
                for k in range(i, j):
                    if dp[i][k] and dp[k+1][j]:
                        dp[i][j] = True
                        break
    # for i in range(n):
    #     print dp[i]

    return dp[0][-1]

stt = 'catsanddogs'

# print check_word_break(stt, obj)
# print word_break_dp(stt, obj)


# print ans
# print "res: ", res
# if obj.search(res):
#     print "Found: ", res
# else:
#     print "No match!"


# Problem: Boggle board
# #####################

### NEED TO REWORK-----NOT PERFECT SOLUTION

# def word_boggle(boggle, words):
#     res, m, n = [], len(boggle), len(boggle[0])

#     visited = [[False]*n for _ in range(m)]

#     for word in words:
#         check_word_in_boggle(boggle, word, visited, m, n, res)
#         print "Visited for str: ", word
#         for i in range(m):
#             print visited[i]

#     return res

# def check_word_in_boggle(boggle, word, visited, m, n, res):
#     if word in words:
#         res.append(word)
#         return

#     for i in range(m):
#         for j in range(n):
#             if not visited[i][j] and word[0] == boggle[i][j]:
#                 check(boggle, word, 0, visited, i, j, m, n, res)

# def check(boggle, word, index, visited, i, j, m, n, res):
#     if index == len(word):
#         print "Heat!"
#         res.append(word)

#     visited[i][j] = True
#     x_coord = [-1, -1, -1, 0, 0, 1, 1, 1]
#     y_coord = [-1, 0, 1, -1, 1, -1, 0, 1]
#     for k in range(8):
#         x = i + x_coord[k]
#         y = j + y_coord[k]
#         if is_valid_move(visited, x, y, m, n) and boggle[x][y] == word[index]:
#             check(boggle, word, index+1, visited, x, y, m, n, res)

# def is_valid_move(visited, x, y, m, n):
#     if x>=0 and x<m and y>=0 and y<n and not visited[x][y]:
#         return True
#     return False


def find_words(boggle, dc, res, m, n, visited, i, j, word):
    visited[i][j] = True
    word += boggle[i][j]
    
    if dc.search(word):
        res.append(word)
        return
    
    x_move = [-1, -1, -1, 0, 0, 1, 1, 1]
    y_move = [-1, 0, 1, -1, 1, -1, 0, 1]

    for k in range(8):
        x = i + x_move[k]
        y = j + y_move[k]

        if x>= 0 and x< m and y>=0 and y<n and not visited[x][y] and dc.isValidWord(word + boggle[x][y]):
            find_words(boggle, dc, res, m, n, visited, x, y, word)

    visited[i][j] = False



def boggle_solve(boggle, dc):
    res = []

    m = len(boggle)
    n = len(boggle[0])

    visited = [[False]*n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if not visited[i][j]:
                find_words(boggle, dc, res, m, m, visited, i, j, "")

    return res

def dfs_word_search(boggle, words, res, m, n, visited, i, j, word):
    if word in words:
        res.append(word)
        return

    visited[i][j] = True
    word += boggle[i][j]

    x_move = [-1, -1, -1, 0, 0, 1, 1, 1]
    y_move = [-1, 0, 1, -1, 1, -1, 0, 1]

    for k in range(8):
        x = i + x_move[k]
        y = j + y_move[k]
        if x>= 0 and x< m and y>=0 and y<n and not visited[x][y]:
            dfs_word_search(boggle, words, res, m, n, visited, x, y, word + boggle[x][y])
    visited[i][j] = False
    # word = word[:-1]


def boggle_dfs(boggle, words):
    res = []

    m = len(boggle)
    n = len(boggle[0])

    visited = [[False]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if not visited[i][j]:
                dfs_word_search(boggle, words, res, m, n, visited, i, j, '')
    return res


boggle = [['g', 'i', 'z'],
          ['u', 'e', 'k'],
          ['q', 's', 'e']]

words = ["geeks", "for", "quiz", "go"]

dictionary = Trie()
for word in words:
    dictionary.insert(word)

# print boggle_solve(boggle, dictionary)
# print boggle_dfs(boggle, words)

# print word_boggle(boggle, words)



# Gas station

class PetrolPump:
    def __init__(self, petrol, distance):
        self.petrol = petrol
        self.distance = distance

def gas_station(arr):
    n = len(arr)
    start = 0
    end = 1
    
    current_petrol = arr[start].petrol - arr[start].distance

    while current_petrol < 0 or end != start:
        while current_petrol < 0 and start != end:
            current_petrol -= arr[start].petrol - arr[start].distance
            start = (start+1)%n

            if start == 0:
                return -1

        current_petrol += arr[end].petrol - arr[end].distance
        end = (end+1)%n

    return start

# arr = [PetrolPump(4, 6), PetrolPump(6, 5), PetrolPump(7, 3), PetrolPump(4, 5)]
arr = [PetrolPump(6, 4), PetrolPump(3, 6), PetrolPump(7, 3)]

# print gas_station(arr)




# Problem: maximum product subarray
#######################################
import sys
def max_product_subarray(arr):
    max_ending_here = 1
    min_ending_here = 1
    flag = 0

    result = 1

    for i in range(len(arr)):
        if arr[i] > 0:
            max_ending_here = max_ending_here*arr[i]
            min_ending_here = min(min_ending_here*arr[i], 1)
            flag = 1
        
        elif arr[i] == 0:
            max_ending_here = 1
            min_ending_here = 1
        
        else:
            tmp = max_ending_here
            max_ending_here = max(min_ending_here*arr[i], 1)
            min_ending_here = tmp*arr[i]

        result = max(result, max_ending_here)

    if flag == 0 and result == 1:
        return 0
    return result

arr = [1, -2, -3, 0, 7, -8, -2]
# print max_product_subarray(arr)


# sorted array to bst
class BSTNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

def sorted_arr_to_bst(arr):
    return _hhh(arr, 0, len(arr)-1)

def _hhh(arr, left, right):
    if left > right:
        return

    mid = (left+right)/2

    root = BSTNode(arr[mid])

    root.left = _hhh(arr, left, mid-1)
    root.right = _hhh(arr, mid+1, right)

    return root

def inorder_bst(root):
    if root is not None:
        inorder_bst(root.left)
        print root.val
        inorder_bst(root.right)


arr = [1, 2, 3, 4, 5]
root = sorted_arr_to_bst(arr)
# print "Root: ", root.val

# inorder_bst(root)



# Problem: Sudoku solver
#######################

def sudoku_solve(board):
  r, c =  checkEmpty(board)
  if r == -1 and c == -1:
    return True
  for val in [1,2,3,4,5,6,7,8,9]:
    if validRow(board, r, val) and validCol(board, c, val) and validSquare(board, r-(r%3), c-(c%3), val):
      board[r][c] = str(val)
      if sudoku_solve(board):
        return True
      board[r][c] = "."
  return False

def checkEmpty(board):
  for r in range(len(board)):
    for c in range(len(board[0])):
      if board[r][c] == ".":
        return r, c
  return -1, -1

def validRow(board, r, val):
  for c in range(len(board[0])):
    if board[r][c] == str(val):
      return False
  return True

def validCol(board, c, val):
  for r in range(len(board)):
    if board[r][c] == str(val):
      return False
  return True

def validSquare(board, r, c, val):
  for i in range(r, r+3):
    for j in range(c, c+3):
      if board[i][j] == str(val):
        return False
  return True


board1 = [[".","8","9",".","4",".","6",".","5"],
         [".","7",".",".",".","8",".","4","1"],
         ["5","6",".","9",".",".",".",".","8"],
         [".",".",".","7",".","5",".","9","."],
         [".","9",".","4",".","1",".","5","."],
         [".","3",".","9",".","6",".","1","."],
         ["8",".",".",".",".",".",".",".","7"],
         [".","2",".","8",".",".",".","6","."],
         [".",".","6",".","7",".",".","8","."]] # false

board2 = [[".",".",".","7",".",".","3",".","1"],
          ["3",".",".","9",".",".",".",".","."],
          [".","4",".","3","1",".","2",".","."],
          [".","6",".","4",".",".","5",".","."],
          [".",".",".",".",".",".",".",".","."],
          [".",".","1",".",".","8",".","4","."],
          [".",".","6",".","2","1",".","5","."],
          [".",".",".",".",".","9",".",".","8"],
          ["8",".","5",".",".","4",".",".","."]] # True


# print "Sudoku solvable? -> ", sudoku_solve(board2)



# input:  S = '1262'
# output: 3
# explanation: There are 3 messages that encode to '1262': 'AZB', 'ABFB', and 'LFB'.

# input:  S = '1270'
# output: 0

def decodeVariations(S):
  n = len(S)
  dp = [0]*(n+1)
  dp[n] = 1
  dp[n-1] = 1 if S[-1] != '0' else 0
  for i in range(n-2, -1, -1):
    if S[i] == '0':
      dp[i] = 0
    if S[i] == '1':
      dp[i] = dp[i+1] + dp[i+2]
    elif S[i] == '2':
      dp[i] = dp[i+1]
      if i+1 < n and S[i+1] <= '6':
        dp[i] += dp[i+2]
    else:
      dp[i] = dp[i+1]
  return dp[0]

# print decodeVariations("1262")
# print decodeVariations("1270")




# Travelling salesman problem
#############################

# Time colplexity - O(n^2*2^n)
def tsp_slove(tsp, cities):
    pass


tsp = [[0, 1, 15, 6],
       [2, 0,  7, 3],
       [9, 6,  0, 12],
       [10,4,  8, 0]]
# print tsp_solve(tsp, 4)



# Dijkstra algo
###############

def dijkstra_solve(djk_matrix, vertices, res):
    pass



djk_matrix = [[0, 6, 0, 1, 0],
              [6, 0, 5, 2, 2],
              [0, 5, 0, 0, 5],
              [1, 2, 0, 0, 1],
              [0, 2, 5, 1, 0]]

res = []
# dijkstra_solve(djk_matrix, 5, res)


def zigzagLevelOrder(A):
    res = []
    
    st = []
    tmp = []
    reverse_flag = False
    st.append(root)
    curr = []
    while st:
        node = st.pop()
        curr.append(node.data)
        if reverse_flag:
            if node.right:
                tmp.append(node.right)
            if node.left:
                tmp.append(node.left)
        else:
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)

        if not st:
            res.append(curr)
            curr = []
            st, tmp = tmp, st
            reverse_flag = not reverse_flag
    return res





# # Problem: Two number sum
# #########################
# from collections import defaultdict
# def two_numbers(arr, k):
#   dct = defaultdict(list)

#   for i in range(len(arr)):
#       if dct.get(k- arr[i]):
#           return k- arr[i], arr[i]
#       dct[arr[i]].append(i)
#   return None

# arr = [3, 0, 5, 1, 4]
# k = 5

# print two_numbers(arr, k)




# Problem: Find closest value in BST
####################################

import os, sys
class BSTNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.helper = [sys.maxint, None]

    def closestNodeVal(self, root, val):
        if root is None:
            return
        if root.data == val:
            self.helper = 0, root.data
            print "Helper: ", self.helper
            return

        diff = abs(root.data - val)
        if self.helper[0] >= diff:
            self.helper = diff, root.data
            print "Helper: ", self.helper
        self.closestNodeVal(root.left, val)
        self.closestNodeVal(root.right, val)

    def wrapper(self, root, val):
        self.closestNodeVal(root, val)
        return self.helper[-1]

    def shit(self, k):
        if k == 1:
            return "1st"
        elif k == 2:
            return "2nd"
        elif k == 3:
            return "3rd"
        else:
            return "{}th".format(k)

    def kth_smallest(self, root, k):
        count = [0]
        return self.kth_smallest_util(root, k, count)

    def kth_smallest_util(self, root, k, count):
        if root is None:
            return

        self.kth_smallest_util(root.left, k, count)
        count[0] += 1
        if count[0] == k:
            print "Found the {} smallest: {}".format(self.shit(k), root.data)
            return
        self.kth_smallest_util(root.right, k, count)

    #   BST
    #    5
    # 3     10
    #     7   15
if __name__ == '__main__':
    root = BSTNode(5)
    root.left = BSTNode(3)
    root.right = BSTNode(10)
    root.right.left = BSTNode(7)
    root.right.right = BSTNode(15)

    # print zigzagLevelOrder(root)

    obj = BST()
    # print obj.wrapper(root, 8)
    # obj.kth_smallest(root, 3)



# # Problem: KMP
# ##############

def build_string_index(pat, tmp):
  j = 0
  i = 1
  while i < len(pat):
      if pat[i] == pat[j]:
          j += 1
          tmp[i] = j
          i += 1
      else:
          if j > 0:
              j = tmp[j-1]
          else:
              tmp[i] = 0
              i += 1

def kmp_search(big_str, pat):
  if len(big_str) == 0 or len(pat) == 0 or len(big_str) < len(pat):
      return -1

  tmp = [0]*len(pat)
  build_string_index(pat, tmp)
  print tmp

  i, j = 0, 0
  while i < len(big_str):
      if big_str[i] == pat[j]:
          i += 1
          j += 1
      if j == len(pat):
          print "Pattern found at index: ", i-j
          j = tmp[j-1]
      elif i < len(big_str) and big_str[i] != pat[j]:
          if j > 0:
              j = tmp[j-1]
          else:
              i += 1
    
txt = "AABAABAAAAAABABAABAAABA"
pat = "AABA"
# kmp_search(txt, pat)




# # Problem: longest increasing subsequence
# # #######################################

# def lis(arr):
#   dp = [1]*len(arr)
#   res = 1
#   for i in range(1, len(arr)):
#       for j in range(i):
#           if arr[j] < arr[i]:
#               dp[i] = max(dp[i], dp[j]+1)
#               res = max(res, dp[i])
#   print "DP: ", dp
#   return res

# def lis_efficient(arr):
#   n = len(arr)
#   tmp = []
#   tmp.append(arr[0])

#   for i in range(1, n):
#       if arr[i] > tmp[-1]:
#           tmp.append(arr[i])
#       else:
#           index = ceil_index(arr, tmp, i)
#           tmp[index] = arr[i]

#   print "TMP: ", tmp
#   return len(tmp)

# def ceil_index(arr, tmp, i):
#   low = 0
#   high = len(tmp) - 1

#   while low < high:
#       mid = (low+high)/2
#       if tmp[mid] < arr[i]:
#           low = mid+1
#       else:
#           high = mid
#   return high

# arr = [5, 1, 4, 3, 9, 6, 2]
# print "LIS: ", lis_efficient(arr)



# # Problem: longest common subsequence
# # ###################################

# def longest_common_subsequence(st1, st2, n1, n2):
#   dp = [[0]*(n1+1) for _ in range(n2+1)]

#   for i in range(1, n2+1):
#       for j in range(1, n1+1):
#           if st2[i-1] == st1[j-1]:
#               dp[i][j] = 1 + dp[i-1][j-1]
#           else:
#               dp[i][j] = max(dp[i-1][j], dp[i][j-1])

#   return dp[-1][-1]


# def lc_subsequence_rec(st1, st2, n1, n2):
#   if n1 == 0 or n2 == 0:
#       return 0
#   elif st1[n1-1] == st2[n2-1]:
#       return 1 + lc_subsequence_rec(st1, st2, n1-1, n2-1)

#   else:
#       return max(lc_subsequence_rec(st1, st2, n1-1, n2), lc_subsequence_rec(st1, st2, n1, n2-1))




# def longest_common_substring(st1, st2, n1, n2):
#   res = 0
#   dp = [[0]*n1 for _ in range(n2)]

#   for i in range(n1):
#       if st1[i] == st2[0]:
#           dp[0][i] = 1
#   for i in range(1, n2):
#       if st1[0] == st2[i]:
#           dp[i][0] = 1

#   for i in range(1, n2):
#       for j in range(1, n1):
#           if st2[i] == st1[j]:
#               dp[i][j] = dp[i-1][j-1] + 1
#               res = max(res, dp[i][j])

#   return res



# def longest_common_substring_rec(st1, st2, n1, n2, c):
#   if n1 == 0 or n2 == 0:
#       return c

#   if st1[n1-1] == st2[n2-1]:
#       c = longest_common_substring_rec(st1, st2, n1-1, n2-1, c+1)

#   c = max(c, longest_common_substring_rec(st1, st2, n1-1, n2, 0), longest_common_substring_rec(st1, st2, n1, n2-1, 0))

#   return c


# st1 = "AGGTAB"
# st2 = "GXTXAB"

# # print lc_subsequence_rec(st1, st2, len(st1), len(st2))
# # print longest_common_subsequence(st1, st2, len(st1), len(st2))
# print longest_common_substring_rec(st1, st2, len(st1), len(st2), 0)
# print longest_common_substring(st1, st2, len(st1), len(st2))


# # Problem: Longest palindromic substring/subsequence
# # ##################################################
# def longest_palindromic_subseq_rec(st, l, r):
#   if l == r:
#       return 1
#   if st[l] == st[r]:
#       if l+1 == r:
#           return 2
#       return 2 + longest_palindromic_subseq_rec(st, l+1, r-1)
#   return max(longest_palindromic_subseq_rec(st, l+1, r), longest_palindromic_subseq_rec(st, l, r-1))

# def longest_palindromic_subseq(st, n):
#   dp = [[0]*n for _ in range(n)]

#   for i in range(n):
#       dp[i][i] = 1
    
#   for l in range(2, n+1):
#       for i in range(n-l+1):
#           j = i+l-1
#           if st[i] == st[j]:
#               dp[i][j] = 2 + dp[i+1][j-1]
#           else:
#               dp[i][j] = max(dp[i][j-1], dp[i+1][j])
#       l += 1

#   for i in range(n):
#       print dp[i]

#   return dp[0][n-1]


# def longest_palindromic_substr(st, n):
#   dp = [[None]*n for _ in range(n)]

#   for i in range(n):
#       dp[i][i] = True

#   start = 0
#   mx_len = 1

#   for i in range(n-1):
#       if st[i] == st[i+1]:
#           dp[i][i+1] = True
#           start = i
#           mx_len = 2

#   for l in range(3, n+1):
#       for i in range(n-l+1):
#           j = i+l-1
#           if st[i] == st[j] and dp[i+1][j-1] == True:
#               dp[i][j] = True
#               start = i
#               mx_len = l
#           else:
#               dp[i][j] = False

#   return st[start: start+mx_len]


# def longest_palindromic_substr_Manachers_algo(st, n):
#   pass

# st = "banana"
# print longest_palindromic_subseq_rec(st, 0, len(st)-1)
# print longest_palindromic_subseq(st, len(st))
# # st = "forgeeksskeegfor"
# print longest_palindromic_substr(st, len(st))




# # Problem: Min jump
# # #################

# def min_jump(arr):
#   n = len(arr)
#   # dp = [0]*n

#   # for i in range(1, n):
#   #   dp[i] = float('inf')
#   #   for j in range(i):
#   #       if arr[j] + j >= i and dp[j] != float('inf'): 
#   #           dp[i] = min(dp[i], dp[j]+1)
#   #           break
#   # print dp
#   # return dp[-1]

#   if n == 0 or arr[0] == 0:
#       return -1
    
#   maxreach = arr[0]
#   steps = arr[0]
#   jumps = 1

#   for i in range(1, n):
#       if i == n-1:
#           return jumps
#       maxreach = max(maxreach, i+arr[i])
#       steps -= 1
#       if steps == 0:
#           jumps += 1
#           if i>maxreach:
#               return -1
#           steps = maxreach - i
#   return jumps

# arr = [4, 3, 0, 1, 2, 5]
# # arr = [1, 3, 6, 1, 0, 9]
# print min_jump(arr)


# # Problem: Heap sort
# # ##################
# def  heapify(arr, n, index):
#   largest = index
#   l = 2*index+1
#   r = 2*index+2

#   if l<n and arr[l] > arr[largest]:
#       largest = l
#   if r<n and arr[r] > arr[largest]:
#       largest = r

#   if largest != index:
#       arr[index], arr[largest] = arr[largest], arr[index]
#       heapify(arr, n, largest)

# def heap_sort(arr):
#   n = len(arr)
#   if n>1:
#       for i in range(n/2, -1, -1):
#           heapify(arr, n, i)
#       for i in range(n-1, 0, -1):
#           arr[i], arr[0] = arr[0], arr[i]
#           heapify(arr, i, 0)

#   return arr

# arr = [3, 5, 2, 1, 4]
# print heap_sort(arr)



# # Problem: Merge sort
# # ###################

# def merge_sort(arr, l, r):
#   if l<r:
#       mid = (l+r)/2
#       merge_sort(arr, l, mid)
#       merge_sort(arr, mid+1, r)
#       return merge(arr, l, mid, r)

#   return arr

# def merge(arr, l, m, r):
#   n1 = m-l+1
#   n2 = r-m
#   L = [None]*n1
#   R = [None]*n2

#   for i in range(n1):
#       L[i] = arr[l+i]
#   for i in range(n2):
#       R[i] = arr[m+1+i]

#   i, j, k = 0, 0, l

#   while i < n1 and j < n2:
#       if L[i] < R[j]:
#           arr[k] = L[i]
#           i += 1
#       else:
#           arr[k] = R[j]
#           j += 1
#       k += 1

#   while i < n1:
#       arr[k] = L[i]
#       i += 1
#       k += 1
#   while j < n2:
#       arr[k] = R[j]
#       j += 1
#       k += 1
#   return arr

# arr = [ 3, 5, 2, 1, 4]
# print merge_sort(arr, 0, len(arr)-1)


# # Problem: Quick sort
# # ###################

# def quick_sort(arr, l, r):
#   if l<r:
#       pi = partition(arr, l, r)
#       quick_sort(arr, l, pi-1)
#       quick_sort(arr, pi+1, r)
#   return arr

# def partition(arr, l, r):
#   pivot = arr[r]
#   p = l-1
#   for i in range(l, r):
#       if arr[i] <= pivot:
#           p += 1
#           arr[i], arr[p] = arr[p], arr[i]
#   p = p+1
#   arr[p], arr[r] = pivot, arr[p]
#   return p

# arr = [3, 5, 2, 1, 4]
# print quick_sort(arr, 0, len(arr)-1)


# # Problem: zigzag traversal
# # #########################
# class BSTNode:
#   def __init__(self, data=None):
#       self.data = data
#       self.left = None
#       self.right = None

# def zigzag(root):
#   res = []
#   if root is None:
#       return res

#   st = []
#   tmp = []
#   reverse_flag = False
#   st.append(root)

#   while st:
#       node = st.pop()
#       res.append(node.data)
#       if reverse_flag:
#           if node.right:
#               tmp.append(node.right)
#           if node.left:
#               tmp.append(node.left)
#       else:
#           if node.left:
#               tmp.append(node.left)
#           if node.right:
#               tmp.append(node.right)

#       if not st:
#           st, tmp = tmp, st
#           reverse_flag = not reverse_flag

#   return res

# #     #    5
# #     # 3     10
# #     #     7   15
# if __name__ == '__main__':
#   root = BSTNode(5)
#   root.left = BSTNode(3)
#   root.right = BSTNode(10)
#   root.right.left = BSTNode(7)
#   root.right.right = BSTNode(15)

#   print zigzag(root)


# # Problem: 0-1 knapsack problem
# # #########################

# def knapSack(weight, wt, val, n):
#   # if weight == 0 or n == 0:
#   #   return 0
#   # if wt[n-1] > weight:
#   #   return knapSack(weight, wt, val, n-1)

#   # return max(val[n-1] + knapSack(weight - wt[n-1], wt, val, n-1), knapSack(weight, wt, val, n-1))

#   dp = [[0]*(weight+1) for i in range(n+1)]

#   for i in range(1, n+1):
#       for j in range(1, weight+1):
#           if wt[i-1] > j:
#               dp[i][j] = dp[i-1][j]
#           else:
#               dp[i][j] = max(dp[i-1][j], val[i-1] + dp[i-1][j-wt[i-1]])
#   return dp[n][weight]

# v = [60, 100, 120]
# wt = [10, 20, 30]
# print knapSack(50, wt, v, 3)

# # Unbounded knapsack problem
# ############################
# # The cake theif
# def max_duffel_bag_value(cake_tuple, weight_capicity):
#     dp = [0]*(weight_capicity+1)
#     for curr_capicity in range(weight_capicity+1):
#         curr_max_value = 0
        
#         for cake_weight, cake_value in cake_tuple:
            
#             if cake_weight == 0 and cake_value != 0:
#                 return float('inf')

#             if cake_weight <= curr_capicity:
#         #         max_val_using_cake = cake_value + dp[curr_capicity - cake_weight]

#         #         curr_max_value = max(curr_max_value, max_val_using_cake)

#         # dp[curr_capicity] = curr_max_value
#                 dp[curr_capicity] = max(dp[curr_capicity], cake_value + dp[curr_capicity - cake_weight])
#         print curr_capicity, dp

#     return dp[-1]

# cake_tuple = [(7, 160), (3, 90), (2, 15)]
# weight_capicity = 20
# print "max_duffel_bag_value: ", max_duffel_bag_value(cake_tuple, weight_capicity)



# Problem: TTiling a recttangle with the fewest squares
memo = dict()
def recur(n, m):
    if n == m:
        return 1
    if (n, m) in memo:
        return memo[(n, m)]

    lmin = min(n, m)
    lmax = max(n, m)
    fmin = 999999999
    val = 0

    for i in range(lmin, 0, -1):
        if i == lmin:
            val = recur(lmax-lmin, lmin)
        else:
            val = min(recur(lmax - i, lmin) + recur(i, lmin - i), recur(lmax - i, i) + recur(lmin - i, lmax))
        if val < fmin:
            fmin = val

    memo[(n, m)] = fmin + 1
    return fmin + 1

# print "Minimun tiles required: ", recur(10, 11)

# Problem: Coin change problem
# ############################

import sys
# min coin required
def min_coin_required(coins, n, target):
    # if target == 0:
    #   return 0

    # res = sys.maxint
    # for i in range(n):
    #   if coins[i] <= target:
    #       sub_res = min_coin_required(coins, n, target-coins[i])
    #       if sub_res != sys.maxint:
    #           res = min(res, sub_res+1)
    # return res

    dp = [[None]*(target+1) for _ in range(n+1)]

    for j in range(target+1):
        dp[0][j] = sys.maxint
    for i in range(1, n+1):
        dp[i][0] = 0

    for i in range(1, n+1):
        for j in range(1, target+1):
            if coins[i-1] <= j:
                dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i-1]] + 1)
            else:
                dp[i][j] = dp[i-1][j]

    return dp[-1][-1]

# number of ways
def num_of_ways(coins, n, target):
    # if target == 0:
    #     return 1
    # if target < 0 or n <= 0:
    #     return 0
    # return num_of_ways(coins, n-1, target) + num_of_ways(coins, n, target-coins[n-1])

    dp = [[None]*(target+1) for _ in range(n+1)]

    for j in range(target+1):
        dp[0][j] = 0
    for i in range(1, n+1):
        dp[i][0] = 1

    for i in range(1, n+1):
        for j in range(1, target+1):
            if coins[i-1] <= j:
                dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[-1][-1]

coins = [1, 2, 3]
target = 5

# print min_coin_required(coins, len(coins), target)
# print num_of_ways(coins, len(coins), target)




# # Problem: permutation of string
# # ##############################
# def permute(arr, l, r):
#   if l == r:
#       print ''.join(arr)

#   for i in range(l, r+1):
#       arr[l], arr[i] = arr[i], arr[l]
#       permute(arr, l+1, r)
#       arr[l], arr[i] = arr[i], arr[l]

# st = "ABC"
# arr = list(st)
# print "Original arr: ", arr
# permute(arr, 0, len(arr)-1)



# Problem: Sliding window
# #######################
# def maximum_number_in_k_size(arr, k):
#   tmp = []
#   for i in range(k):
#       while tmp and arr[tmp[-1]]<arr[i]:
#           tmp.pop(-1)
#       tmp.append(i)
#   print "TMP: {}, max = {}".format(tmp, arr[tmp[0]])
#   for i in range(k, len(arr)):
      
#       while tmp and tmp[0] <= i - k:
#           tmp.pop(0)

#       while tmp and arr[tmp[-1]]<arr[i]:
#           tmp.pop(-1)
#       tmp.append(i)
#       print "TMP: {}, max = {}".format(tmp, arr[tmp[0]])

# arr = [1, 2, 3, 1, 5, 4, 2, 3, 6]
# maximum_number_in_k_size(arr, 3)
# 
# import sys
# def minimum_window_contains_all_own_str_char(str):
#   table = [0]*256

#   target_chrs = set(list(str))
#   # print "Target: ", target_chrs
#   curr_count = 0
#   start = 0
#   starting_index = start
#   min_len = sys.maxint
#   for i in range(len(str)):
#       table[ord(str[i])] += 1
#       if table[ord(str[i])] == 1:
#           curr_count += 1

#       if curr_count == len(target_chrs):
#           while table[ord(str[start])] > 1:
#               table[ord(str[start])] -= 1
#               start += 1
#           if i-start < min_len:
#               min_len = min(min_len, i-start)
#               starting_index = start
#   return str[starting_index: starting_index+min_len+1]

# def min_window_for_pattern(str, pat):
#   pat_table = [0]*256
#   str_table = [0]*256

#   for i in range(len(pat)):
#       pat_table[ord(pat[i])] += 1
#   curr_count = 0
#   start = 0
#   starting_index = start
#   min_len = sys.maxint
#   for i in range(len(str)):
#       str_table[ord(str[i])] += 1

#       if str_table[ord(str[i])] != 0 and str_table[ord(str[i])] <= pat_table[ord(str[i])]:
#           curr_count += 1

#       if curr_count == len(pat):
#           while str_table[ord(str[start])] > pat_table[ord(str[start])] or pat_table[ord(str[start])] == 0:
#               if str_table[ord(str[start])] > pat_table[ord(str[start])]:
#                   str_table[ord(str[start])] -= 1
#               start += 1
#           if i-start < min_len:
#               min_len = min(min_len, i-start)
#               starting_index = start
    
#   return str[starting_index: starting_index+min_len+1]


# str = "abdbcscabdcsadb"
# pat = "abcd"
# # print minimum_window_contains_all_own_str_char(str)
# print min_window_for_pattern(str, pat)


# Problem: Find the celebrity
#############################

# def find_celebrity(matrix, n):
#   candidate = 0
#   for i in range(1, n):
#       if matrix[candidate][i]:
#           candidate = i

#   for i in range(n):
#       if candidate != i and matrix[candidate][i] and not matrix[i][candidate]:
#           return None
#   return candidate

# if __name__ == '__main__':
#   celebrity_matrix = [[0, 0, 1, 0],
#                       [0, 0, 1, 0],
#                       [0, 0, 0, 0],
#                       [0, 0, 1, 0]
#                      ]
#   n = len(celebrity_matrix)
#   print "Celebrity ID:", find_celebrity(celebrity_matrix, n)


# # Grid problem
# ##############

# def min_cost(matrix):
#   m = len(matrix)
#   n = len(matrix[0])

#   dp = [[0]*n for _ in range(m)]
#   dp[0][0] = matrix[0][0]
    
#   for i in range(1, m):
#       dp[i][0] = dp[i-1][0] + matrix[i][0]

#   for j in range(1, n):
#       dp[0][j] = dp[0][j-1] + matrix[0][j]

#   for i in range(1, m):
#       for j in range(1, n):
#           dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + matrix[i][j]

#   return dp[m-1][n-1]

# cost = [[1, 2, 3], 
#         [4, 8, 2], 
#         [1, 5, 3]]

# print min_cost(cost)



# def num_of_ways(matrix):
#   m = len(matrix)
#   n = len(matrix[0])

#   dp = [[0]*n for _ in range(m)]

#   for i in range(m):
#       if matrix[i][0] == 1:
#           break
#       dp[i][0] = 1

#   for j in range(1, n):
#       if matrix[0][j] == 1:
#           break
#       dp[0][j] = 1

#   for i in range(1, m):
#       for j in range(1, n):
#           if matrix[i][j] == 1:
#               continue
#           dp[i][j] = dp[i-1][j] + dp[i][j-1]

#   print "DP:"
#   for i in range(m):
#       print dp[i]
#   return dp[-1][-1]

# matrix = [[0, 1, 0], 
#           [0, 0, 0], 
#           [1, 0, 0]]
# print num_of_ways(matrix)


# # Problem: Find no of islands
# # ###########################

# def number_of_island(matrix):
#   m = len(matrix)
#   n = len(matrix[0])
#   count = 0
#   visited = [[False]*n for _ in range(m)]
#   for i in range(m):
#       for j in range(n):
#           if matrix[i][j] == 1 and not visited[i][j]:
#               dfs(matrix, i, j, m, n, visited)
#               count += 1
#   return count

# def dfs(matrix, i, j, m, n, visited):
#   visited[i][j] = True
#   x = [-1, -1, -1, 0, 0, 1, 1, 1]
#   y = [-1, 0, 1, -1, 1, -1, 0, 1]
#   for k in range(8):
#       curr_x = i + x[k]
#       curr_y = j + y[k]
#       if curr_x >= 0 and curr_x < m and curr_y >= 0 and curr_y < n and matrix[curr_x][curr_y] == 1 and not visited[curr_x][curr_y]:
#           dfs(matrix, curr_x, curr_y, m, n, visited)

# matrix = [[1, 0, 1, 0, 1],
#                [0, 1, 0, 1, 0],
#      [0, 0, 0, 0, 0],
#      [1, 1, 0, 0, 0],
#      [0, 1, 1, 0, 1]
#   ]

# print number_of_island(matrix)
# for i in range(len(matrix)):
#   print matrix[i]



# # Problem: median of stream of integers
# #######################################

# from heapq import heapify, heappush, heappop
# class Stream:
#   def __init__(self):
#       self.min_heap = []
#       heapify(self.min_heap)
#       self.max_heap = []
#       heapify(self.max_heap)
#       self.median = None

#   def process_stream(self, arr):
#       self.median = arr[0]
#       print "median: ", self.median
#       heappush(self.min_heap, arr[0])

#       for i in range(1, len(arr)):

#           ele = arr[i]
#           if len(self.min_heap) > len(self.max_heap):
#               if ele < self.median:
#                   val = heappop(self.min_heap)
#                   heappush(self.max_heap, -1*val)
#                   heappush(self.min_heap, ele)
#               else:
#                   heappush(self.max_heap, -1*ele)

#               self.median = (self.min_heap[0] - self.max_heap[0])//2
                    
#           elif len(self.min_heap) == len(self.max_heap):
#               if ele < self.median:
#                   heappush(self.min_heap, ele)
#                   self.median = self.min_heap[0]
#               else:
#                   heappush(self.max_heap, -1*ele)
#                   self.median = - self.max_heap[0]
            
#           else:
#               if ele < self.median:
#                   heappush(self.min_heap, ele)
#               else:
#                   val = -1* heappop(self.max_heap)
#                   heappush(self.min_heap, val)
#                   heappush(self.max_heap, -1*ele)

#               self.median = (self.min_heap[0] - self.max_heap[0])//2

#           print "median: ", self.median


# arr = [5, 15, 10, 20, 3]
# obj = Stream()
# obj.process_stream(arr)



# # Problem: optimal strategy game
# # ##############################

# class Data:
#   def __init__(self):
#       self.first = None
#       self.seconf = None

# def game(arr):
#   n = len(arr)

#   dp = [[None]*n for _ in range(n)]
#   for i in range(n):
#       dp[i][i] = [arr[i], 0]

#   for l in range(2, n+1):
#       for i in range(n-l+1):
#           j = i+l-1
#           if arr[i] + dp[i+1][j][1] > arr[j] + dp[i][j-1][1]:
#               dp[i][j] = [arr[i] + dp[i+1][j][1], dp[i+1][j][0]]
#           else:
#               dp[i][j] = [arr[j] + dp[i][j-1][1], dp[i][j-1][0]]

#   for i in range(n):
#       print dp[i]

#   return dp[0][-1]

# def game_rec(arr, start, end):
#   if start > end:
#       return 0
#   if start == end:
#       return arr[start]
#   if start + 1 == end:
#       return max(arr[start], arr[end])

#   a = arr[start] + min(game_rec(arr, start+2, end), game_rec(arr, start+1, end-1))
#   b = arr[end] + min(game_rec(arr, start, end-2), game_rec(arr, start+1, end-1))

#   return max(a, b)

# arr = [3, 9, 1, 2]
# # arr = [20, 30, 2, 2, 2, 10]
# res = game(arr)
# print "First = {0}, second = {1}".format(res[0], res[1])

# print "Recursion: ", game_rec(arr, 0, len(arr)-1)


# def two_sum(arr, k):
#   dp = dict()

#   for i in range(len(arr)):
#       if dp.get(arr[i]) != None:
#           return [dp.get(arr[i]), i]
#       dp[k-arr[i]] = i
#       print "DP: ", dp

#   return []

# arr = [2, 7, 11, 15]
# print two_sum(arr, 9)


# def merge(arr1, arr2):
#   big = len(arr1)
#   small = len(arr2)

#   pos = big-1

#   i = big-small-1
#   j = small-1

#   while i >= 0 and j >= 0:
#       if arr1[i] > arr2[j]:
#           arr1[pos] = arr1[i]
#           i -= 1
#       else:
#           arr1[pos] = arr2[j]
#           j -= 1
#       pos -= 1

#   while j >= 0:
#       arr1[pos] = arr2[j]
#       j -= 1
#       pos -= 1

#   return arr1

# arr1 = [5, 6, 9, 10, None, None, None]
# arr2 = [3, 4, 8]

# print merge(arr1, arr2)



# def equal_0and1(st):
#   dct = dict()
#   dct[0] = 0

#   count = 0
#   res, start, end = 0, 0, 0
#   for i in range(len(st)):
#       if st[i] == '0':
#           count += 1
#       else:
#           count -= 1

#       if dct.get(count):
#           if i - dct[count] > res:
#               res = i - dct[count]
#               start = dct[count]
#               end = i
#       else:
#           dct[count] = i

#   return [res, start, end]

# st = '01001101'
# result = equal_0and1(st)
# print result




# # Longest consecutive subsequence elements in and array

# def longest_consecutive_subsequence(arr):
#     s = set()
#     for e in arr:
#         s.add(e)
#     res = 1
#     for i in range(len(arr)):
#         if arr[i]-1 not in s:
#             curr = arr[i]
#             while curr in s:
#                 curr += 1
#             res = max(res, curr - arr[i])
#     return res

# arr = [1, 9, 3, 10, 4, 20, 2]
# print longest_consecutive_subsequence(arr)





