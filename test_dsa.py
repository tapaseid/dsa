import os, sys

# Find kth smallest element from row and column wise sorted matrix
def find_kth_element(mat, m, n, k):
    lr, lc = 1, 0
    rr, rc = 0, 1
    count = 1
    r, c = 0, 0
    if k == 1:
        return mat[r][c]
        
    while count < k:
        count += 1
        if mat[lr][lc]<= mat[rr][rc]:
            r, c = lr, lc
            if lr < m-1:
                lr += 1
            else:
                if lc < n-1:
                    lc += 1
                if rr < m-1:
                    lr = rr+1
        else:
            r, c = rr, rc
            if rc < n-1:
                rc += 1
            else:
                if rr < m-1:
                    rr += 1
                if lc < n-1:
                    rc = lc+1
    return mat[r][c]

mat = [
       [1, 3, 5],
       [2, 6, 9],
       [3, 6, 9]
      ]
print find_kth_element(mat, len(mat), len(mat[0]), 6)
sys.exit(0)


def gcd(x, y):
    if x%y == 0:
        return y
    return gcd(y, x/y)
print gcd(8, 4)
sys.exit(0)



class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print root.data,
        inorder(root.right)

# def fun(inorder, preorder, n):
#     res = []
#     postorder(inorder, preorder, 0, n-1, res)
#     return res

# def postorder(inorder, preorder, l, r, res):
#     if l<r:
#         root = preorder[0]
#         index = inorder.index(root)
#         postorder(inorder[:index], preorder[1:index+1], l, index-1, res)
#         postorder(inorder[index+1:], preorder[index+1:], index+1, r, res)

#         res.append(root)

# inorder = [4, 2, 5, 1, 3, 6]
# preorder = [1, 2, 4, 5, 3, 6]
# print fun(inorder, preorder, len(inorder))

def serialize(root, lst):
    if root is None:
        lst.append('-')
        return
    lst.append(root.data)
    serialize(root.left, lst)
    serialize(root.right, lst)

def deserialize(lst):
    if not len(lst):
        return 
    if lst[0] == '-':
        lst = lst[1:]
        return
    root = Node(lst[0])
    lst = lst[1:]
    root.left = deserialize(lst)
    root.right = deserialize(lst)

    return root


def left_view(root, level, mx_level):
    if root is None:
        return
    if mx_level[0] < level:
        print root.data
        mx_level[0] = level
    left_view(root.left, level+1, mx_level)
    left_view(root.right, level+1, mx_level)

def bt_to_dll(root, head, prev):
    if root is None:
        return

    bt_to_dll(root.left, head, prev)

    if prev[0] is None:
        head = root
    else:
        root.left = prev[0]
        prev[0].right = root
        prev[0] = root
        print head.data
    bt_to_dll(root.right, head, prev)

def print_list(head):
    while head is not None:
        print head.data,
        head = head.right

root = Node(10)
root.left = Node(12)
root.right = Node(15)
# root.left.left = Node(25)
root.left.right = Node(30)
root.right.left = Node(36)

lst = []
serialize(root, lst)
print lst
root = deserialize(lst)

inorder(root)

sys.exit(0)

mx_level = [0]
left_view(root, 1, mx_level)

inorder(root)
print
head = None
prev = [None]
bt_to_dll(root, head, prev)
print_list(head)

sys.exit(0)



def build_tree(inord, preord):
    mp = {}
    n = len(inord)
    for i in range(n):
        mp[inord[i]] = i

    return _build_tree_helper(inord, preord, 0, n-1, mp, 0)


def _build_tree_helper(inord, preord, in_s, in_e, mp, pind):
    if in_s>in_e:
        return None

    curr = preord[pind]
    tmp_node = Node(curr)
    if in_s==in_e:
        return tmp_node

    index = mp[curr]

    tmp_node.left = _build_tree_helper(inord, preord, in_s, index-1, mp, pind+1)
    tmp_node.right = _build_tree_helper(inord, preord, index+1, in_e, mp, pind+1)

    return tmp_node

inorder = [4, 2, 5, 1, 3, 6]
preorder = [1, 2, 4, 5, 3, 6]
root = build_tree(inorder, preorder)
print root.right.data
# inorder(root)



import sys, os
def kthsmallest(root, k):
    stack = []*k
    while True:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()
        if k == 1:
            return root.data
        else:
            k -= 1
            root = root.right


root = Node(2)
root.left = Node(1)
root.right = Node(3)
print kthsmallest(root, 2)


def remove_single_child(root):
    if root is None:
        return

    root.left = remove_single_child(root.left)
    root.right = remove_single_child(root.right)

    if root.left is None and root.right is None:
        return root

    if root.left is None:
        new_root = root.right
        root = None
        return new_root

    if root.right is None:
        new_root = root.left
        root = None
        return new_root

    return root

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

inorder(root)
print
remove_single_child(root)
inorder(root)


def calculate_span(arr):
    n = len(arr)
    res = [0 for _ in range(n)]
    st = []
    st.append(0)
    res[0] = 1
    for i in range(1, n):
        while len(st) and arr[st[-1]]<arr[i]:
            st.pop()
        res[i] = i+1 if not len(st) else i-st[-1]
        st.append(i)
    return res

arr = [100, 80, 60, 70, 60, 75, 85]
# print calculate_span(arr)

def next_greater_element(arr):
    n = len(arr)
    s = []
    d = {}
    s.append(arr[0])
    for i in range(1, n):
        if len(s):
            nxt = arr[i]
            element = s.pop()
            while element < nxt:
                d[element] = nxt
                if not len(s):
                    break
                element = s.pop()
            if element>nxt:
                s.append(element)
        s.append(arr[i])
    while len(s):
        d[s.pop()] = -1
    for i in arr:
        print "{}--->{}".format(i, d.get(i))

# arr = [13, 7, 6, 12]
# next_greater_element(arr)


def _helper_dfs(grid, r, c, row, col):
    if r == 0 and c == col-1:
        return grid[r][c]

    if r>=0 and c<col-1:
        north = _helper_dfs(grid, r, c+1, row, col)
    else:
        north = 0
    if r>0 and c<col:
        east = _helper_dfs(grid, r-1, c, row, col)
    else:
        east = 0
    return max(north, east) + grid[r][c]

def mx_count_dfs(grid, row, col):
    return _helper_dfs(grid, row-1, 0, row, col)


def max_cost(grid, row, col):
    mat = [[0]*col for _ in range(row)]
    mat[row-1][0] = grid[row-1][0]
    for j in range(1, col):
        mat[row-1][j] = mat[row-1][j-1] + grid[row-1][j]
    for i in range(row-2, -1, -1):
        mat[i][0] = mat[i+1][0] + grid[i][0]

    for i in range(row-2, -1, -1):
        for j in range(1, col):
            mat[i][j] = max(mat[i][j-1], mat[i+1][j]) + grid[i][j]
            # print mat
    return mat[0][col-1]

grid = [[0, 0, 0, 0, 5], [0, 1, 1, 1, 0], [2, 0, 0, 0, 0]]
# print max_cost(grid, len(grid), len(grid[0]))
# print mx_count_dfs(grid, len(grid), len(grid[0]))

def first_repeating(s):
    repeated = [False]*256
    lookups = []

    for i in range(len(s)):
        # if not repeated[ord(s[i])]:
        if not s[i] in lookups:
            lookups.append(s[i])
        else:
            lookups.remove(s[i])
        if len(lookups):
            print lookups[0]

s = 'geeksforgeeksandgeeksquizfor'
# first_repeating(s)

#sherlock and anagream

def sherlock_and_anagram(s):
    from collections import defaultdict
    check = defaultdict(int)
    l = len(s)
    for i in range(l):
        for j in range(i+1,l+1):
            sub = list(s[i:j])
            sub.sort()
            sub = "".join(sub)
            check[sub]+=1
    sum = 0
    for i in check:
        n = check[i]
        sum += (n*(n-1))/2
    return sum

s = 'abba'
# print sherlock_and_anagram(s)




def minimum_swaps(arr):
    n = len(arr)
    count = 0
    i = 0
    while i < n:
        if arr[i] == i+1:
            i += 1
            continue
        arr[i], arr[arr[i]-1] = arr[arr[i]-1], arr[i]
        count += 1

    return count

def min_swap(arr):
    n = len(arr)
    arr_c = list(enumerate(arr))
    arr_c.sort(key=lambda x: x[1])
    count = 0
    visited = [False]*n
    for i in range(n):
        if visited[i] or arr_c[i][0] == i:
            continue
        c = 0
        v = i
        while not visited[v]:
            visited[v] = True
            v = arr_c[v][0]
            c += 1
        if c>0:
            count += c-1
    return count


def merge(arr, tmp, l, m, r):

    i, j, k = l, m+1, l
    count = 0
    while i<=m and j<=r:
        if arr[i]<arr[j]:
            tmp[k] = arr[i]
            i += 1
        else:
            tmp[k] = arr[j]
            j += 1
            count += m+1-i
        k+= 1

    while i<=m:
        tmp[k] = arr[i]
        i += 1
        k += 1
    while j<=r:
        tmp[k] = arr[j]
        j += 1
        k += 1
    for i in range(l, r+1):
        arr[i] = tmp[i]

    return count 



def _helper(arr, tmp, l, r):
    swaps = 0
    if l<r:
        m = (l+r)/2
        swaps = _helper(arr, tmp, l, m)
        swaps += _helper(arr, tmp, m+1, r)
        swaps += merge(arr, tmp, l, m, r)
    return swaps
        

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    n = len(arr)
    tmp = [None]*n
    return _helper(arr, tmp, 0, n-1)

arr = [7, 1, 3, 2, 4, 5, 6]
# print min_swap(arr)
# print minimum_swaps(arr)


def bribe(q):
    n = len(q)
    bribe = 0
    chaotic = False
    for i in range(n):
        if q[i]-i-1 > 2:
            chaotic = True
            break
        index = max(0, q[i]-2)
        for j in range(index, i):
            if q[j] > q[i]:
                bribe += 1
    if chaotic:
        return "Too chaotic"
    else:
        return bribe



# q = [2, 1, 5, 4, 3]
# print bribe(q)


def is_safe(i, j, m, n):
    if i>=0 and i<m and j>=0 and j<n:
        return True
    return False
# Complete the hourglassSum function below.
def hourglassSum(arr):
    m = len(arr)
    n = len(arr[0])
    row = [-1, -1, -1, 0, 1, 1, 1]
    col = [-1, 0, 1, 0, -1, 0, 1]
    max_sum = 0
    for i in range(1, m-1):
        for j in range(1, n-1):
            sm = 0
            for k in range(7):
                sm += arr[i+row[k]][j+col[k]]

            max_sum = max(max_sum, sm)
    return max_sum

arr = [[1, 1, 1, 0, 0, 0],
      [0, 1, 0, 0, 0, 0],
      [1, 1, 1, 0, 0, 0],
      [0, 0, 2, 4, 4, 0],
      [0, 0, 0, 2, 0, 0],
      [0, 0, 1, 2, 4, 0]]

# print hourglassSum(arr)


def repeatedString(s, n):
    lst = []
    len_s = len(s)
    for i in range(len(s)):
        if s[i] == 'a':
            lst.append(i)
    # print lst
    count = 0
    q = n/len_s
    r = n%len_s

    count += q*len(lst)
    for j in lst:
        if j<r:
            count += 1

    return count

# s = 'aba'
# n = 10
# print repeatedString(s, n)



def leave_paths(root):
    if root is None:
        return


def jumpingOnClouds(c):
    n = len(c)
    d = [i for i in range(n)]
    # d[0] = 0
    for i in range(n):
        print "{}-----{}".format(i, d)
        if c[i] == 1:
            d[i] = d[i-1]
            continue
        if i+2 < n and c[i+2]==0:
            d[i+2] = min(d[i+2], d[i]+1)
        if i+1 < n and c[i+1]==0:
            d[i+1] = min(d[i+1], d[i]+1)

    return d[n-1]



# c = [0, 0, 0, 0, 1, 0]
# print jumpingOnClouds(c)











class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


def mirror_tree(root):
    if root is None:
        return
    if root.left or root.right:
        tmp = root.left
        root.left = root.right
        root.right = tmp
        mirror_tree(root.left)
        mirror_tree(root.right)
    return root

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print root.data,
    inorder(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
# root.right.left = Node(6)

# inorder(root)
# print 
# root = mirror_tree(root)
# inorder(root)




# class Node:
#   def __init__(self, x, y, steps):
#       self.x = x
#       self.y = y
#       self.steps = steps


# def is_safe(x, y, n):
#   if x>=1 and x<= n and y>=1 and y<=n:
#       return True
#   return False

# def min_knight_steps(knight_pos, target_pos, n):
#   dx = [-2, -1, 1, -2, 2, -1, 1, 2]
#   dy = [-1, -2, -2, -1, 1, 2, 2, 1]

#   visit = [[False]*(n+1) for i in range(n+1)]
#   q = []

#   q.append(Node(knight_pos[0], knight_pos[1], 0))

#   while len(q):
#       t = q.pop(0)
#       if t.x==target_pos[0] and t.y==target_pos[1]:
#           print t.steps
#           return
#       for i in range(8):
#           x = t.x + dx[i]
#           y = t.y + dy[i]

#           if is_safe(x, y, n) and not visit[x][y]:
#               visit[x][y] = True
#               q.append(Node(x, y, t.steps+1))

# if __name__ == '__main__':
#   n = 30
#   knight_pos = [4, 5]
#   target_pos = [1, 1]
#   min_knight_steps(knight_pos, target_pos, n)





# class Node:
#   def __init__(self, data=None):
#       self.data = data
#       self.left = None
#       self.right = None

# class BST:
#   def insert(self, root, key):
#       if root is None:
#           return Node(key)
#       if root.data < key:
#           if root.right is None:
#               root.right = Node(key)
#           else:
#               root.right = self.insert(root.right, key)
#       else:
#           if root.left is None:
#               root.left = Node(key)
#           else:
#               root.left = self.insert(root.left, key)

#       return root

#   def inorder(self, root):
#       if root is not None:
#           self.inorder(root.left)
#           print root.data,
#           self.inorder(root.right)

#   def lavel_order(self, root):
#       h = self.height(root)
#       # print "Height: ", h
#       for i in range(1, h+1):
#           self.print_given_lavel(root, i)

#   def print_given_lavel(self, root, lavel):
#       if root is None:
#           return
#       if lavel == 1:
#           print root.data,
        
#       self.print_given_lavel(root.left, lavel-1)
#       self.print_given_lavel(root.right, lavel-1)

#   def height(self, root):
#       if root is None:
#           return 0
#       return 1 + max(self.height(root.left), self.height(root.right))

#   def lavel_order_iterative(self, root):
#       if root is None:
#           return
#       q = []
#       q.append(root)

#       while len(q):
#           node = q.pop(0)
#           print node.data,
#           if node.left:
#               q.append(node.left)
#           if node.right:
#               q.append(node.right)

# from collections import defaultdict
# class Graph:
#   def __init__(self):
#       self.graph = defaultdict(list)

#   def add(self, u, v):
#       self.graph[u].append(v)

#   def count_dependency(self):
#       print self.graph
#       count = 0
#       for i in self.graph:
#           count += len(self.graph[i])
#       return count


# if __name__ == '__main__':
#   arr = [5, 1, 4, 9, 10, 3, 6, 2]

#   obj = BST()
#   root = None
#   for i in arr:
#       root = obj.insert(root, i)

#   # print root.data

#   # obj.inorder(root)
#   obj.lavel_order(root)
#   print
#   obj.lavel_order_iterative(root)

#   graph = Graph()
#   graph.add(0, 3)
#   graph.add(0, 2)
#   graph.add(1, 2)
#   graph.add(3, 2)

#   print graph.count_dependency()



# def min_diff_among_m_elements(arr, m, n):
#   arr.sort()
#   print arr
#   ans = arr[m-1]-arr[0]

#   for i in range(1, n-m+1):
#       diff = arr[m-1+i]-arr[i]
#       ans = min(ans, diff)

#   return ans

# # arr = [7, 3, 2, 4, 9, 12, 56]
# # m = 3

# arr = [3, 4, 1, 9, 56, 7, 9, 12]
# m = 5

# # arr = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
# # m = 7

# n = len(arr)
# print min_diff_among_m_elements(arr, m, n)


# class TrieNode:
#   def __init__(self):
#       self.children = [None]*26
#       self.isEndOfWord = False

# class Trie:
#   def __init__(self):
#       self.root = self.getNode()

#   def getNode(self):
#       return TrieNode()

#   def _charToIndex(self, ch):
#       return ord(ch) - ord('a')


#   def insert(self, word):
#       tmp = self.root
#       n = len(word)
#       for i in range(n):
#           index = _charToIndex(word[i])
#           if not tmp.children[index]:
#               tmp.children[index] = self.getNode()
#           tmp = tmp.children[index]

#       tmp.isEndOfWord = True


#   def search(self, word):
#       pass

#   def delete(self, word):
#       pass

#   def display(self):
#       pass

#   def count(self):
#       pass

# if __name__ == '__main__':
#   input_arr = ['the', 'thought', 'there', 'fcuk', 'fcma']

#   trie = Trie()

#   for i in input_arr:
#       trie.insert(i)


# def remove_duplicate(arr, n):
#   d = {}
#   req_arr = []
#   for i in range(n):
#     if arr[i] in d:
#       continue
#     req_arr.append(arr[i])
#     d[arr[i]] = 1
    
#   for i in req_arr:
#     print i,
    
# n = int(raw_input().strip())
# arr = map(int, raw_input().strip().split(' '))
# remove_duplicate(arr, n)

# DCT = {}
# def prime(p):
#   flag = 1
#   for i in range(2, p/2+1):
#       if p%i == 0:
#           flag = 0
#           break
#   return flag

# import math
# def xyz(n):
#   flag = 0
#   i = 2
#   while i >=2 and i <= int(math.sqrt(n))+14:
#       if DCT.get(i):
#           if i*(i+14) == n or i*(i-14) == n:
#               flag = 1
#               # break
#           i += 1
#       elif prime(i):
#           DCT[i] = 1
#       else: i += 1
            

#   return flag

# count = 0
# for i in range(1000000):
#   if xyz(i):
#       # print "{}, {}".format(i, DCT)
#       count += 1
# print count

# def _check(i):
#   s = str(i)
#   for i in range(len(s)-1):
#       if int(s[i]) > int(s[i+1]):
#           print s
#           return False
#   return True

# def get_count(n):
#   count = 0
#   for i in range(1, n+1):
#       if _check(i):
#           count += 1

#   return count

# print get_count(21)


