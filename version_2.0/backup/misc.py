## Burst baloon

# int Solution::solve(vector<int> &A) {
#     int n = A.size();
#     vector<vector<int> > dp(n, vector<int>(n, 0));
    
#     for(int len = 1; len <= A.size(); len++){
        
#         for(int i = 0; i <= A.size() - len; i++){
#             int j = i + len - 1;
            
#             for(int k = i; k <= j; k++){
#                 int before = 0;
#                 int after = 0;
#                 int left = 1;
#                 int right = 1;
                
#                 if(i != 0){
#                     left = A[i - 1]; 
#                 }
                
#                 if(j != n - 1){
#                     right = A[j + 1];
#                 }
                
#                 if(k != i){
#                     before = dp[i][k - 1];
#                 }
                
#                 if(k != j){
#                     after = dp[k + 1][j];
#                 }
                
#                 dp[i][j] = max(dp[i][j], before + after + left * A[k] * right);
                
#             }
#         }
#     }
    
#     return dp[0][n - 1];
# }


# Gold mine problem

def get_max_gold(gold):
    row, col = len(gold), len(gold[0])
    ans = 0

    def max_gold_rec(r, c):
        if c >= col or r < 0 or r >= row:
            return 0

        x = max_gold_rec(r+1, c+1)
        y = max_gold_rec(r-1, c+1)
        z = max_gold_rec(r, c+1)

        return gold[r][c] + max(x, y, z)

    for i in range(row):
        ans = max(ans, max_gold_rec(i, 0))

    return ans

def get_max_gold_dp(gold):
    row, col = len(gold), len(gold[0])

    dp = [[0]*col for _ in range(row)]

    for i in range(row):
        dp[i][0] = gold[i][0]

    for j in range(1, col):
        for i in range(row):
            x = dp[i - 1][j - 1] if i - 1 >= 0 else 0
            y = dp[i][j - 1]
            z = dp[i + 1][j - 1] if i + 1 < row else 0

            dp[i][j] = gold[i][j] + max(x, y, z)

    res = 0
    for i in range(row):
        res = max(res, dp[i][col - 1])
    return res

gold = [[1, 3, 1, 5],
        [2, 2, 4, 1],
        [5, 0, 2, 3],
        [0, 6, 1, 2]]

print get_max_gold_dp(gold)





import sys, os

def permute(A):
        n = len(A)
        
        res = []
        _helper(A, n, 0, res)
        return res
import pdb        
def _helper(arr, size, index, res):
    if index == size-1:
        res.append(list(arr))
        return
    # pdb.set_trace()
    for i in range(index, size):
        arr[index], arr[i] = arr[i], arr[index]
        _helper(arr, size, index+1, res)
        arr[index], arr[i] = arr[i], arr[index]

A = [1, 2, 3]
# print permute(A)


# LFU cache
class LFU:
    def __init__(self, capacity):
        self.dct = dict()
        self.freq_table = dict()
        self.capacity = capacity
        self.count = 0
        self.min_freq = 0

    def get(self, key):
        if key not in self.dct:
            return -1

        val, curr_freq = self.dct.get(key)
        self.dct[key] = (val, curr_freq + 1)

        curr_freq_list = self.freq_table.get(curr_freq)
        curr_freq_list.remove(key)

        next_freq_list = self.freq_table.get(curr_freq + 1, [])
        next_freq_list.insert(0, key)
        self.freq_table[curr_freq + 1] = next_freq_list

        if len(curr_freq_list) == 0 and curr_freq == self.min_freq:
            self.min_freq += 1
        
        return val

    def put(self, key, val):
        if self.capacity == 0:
            return

        if key in self.dct:
            val, curr_freq = self.dct.get(key)
            self.dict[key] = (val, curr_freq + 1)

            curr_freq_list = self.freq_table.get(curr_freq)
            curr_freq_list.remove(key)

            next_freq_list = self.freq_table.get(curr_freq + 1, [])
            next_freq_list.insert(0, key)
            self.freq_table[curr_freq + 1] = next_freq_list

            if len(curr_freq_list) == 0 and curr_freq == self.min_freq:
                self.min_freq += 1
            
            return

        if self.capacity == self.count:
            freq_bin = self.freq_table[self.min_freq]
            k = freq_bin.pop()
            del self.dct[k]
            self.count -= 1

        self.dct[key] = (val, 1)
        freq_bin = self.freq_table.get(1, [])
        freq_bin.insert(0, key)
        self.count += 1
        self.freq_table[1] = freq_bin
        self.min_freq = 1
        return


# lfu_obj = LFU(3)
# lfu_obj.put(1, 11)
# print "Put: {}---{}---{}".format(1, lfu_obj.dct, lfu_obj.freq_table)
# lfu_obj.put(2, 22)
# print "Put: {}---{}---{}".format(2, lfu_obj.dct, lfu_obj.freq_table)
# lfu_obj.put(3, 33)
# print "Put: {}---{}---{}".format(3, lfu_obj.dct, lfu_obj.freq_table)
# print lfu_obj.get(1)
# print "Get: {}---{}---{}".format(1, lfu_obj.dct, lfu_obj.freq_table)
# lfu_obj.put(4, 44)
# print "Put: {}---{}---{}".format(4, lfu_obj.dct, lfu_obj.freq_table)



# count smaller elements on right side
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.eleCount = 1
        self.lCount = 0

class CountSmaller:
    def __init__(self, root):
        self.root = root

    def insert(self, node):
        curr = self.root
        count = 0
        while curr:
            prev = curr

            if node.val < curr.val:
                curr.lCount += 1
                curr = curr.left

            elif node.val > curr.val:
                count += curr.eleCount + curr.lCount
                curr = curr.right
            else:
                prev = curr
                curr.eleCount += 1
                break

        if prev.val < node.val:
            prev.right = node
        elif prev.val > node.val:
            prev.left = node
        else:
            return count + prev.lCount

        return count

arr = [10, 6, 15, 7, 20, 30, 5, 7]
n = len(arr)
ans = [0]

obj = CountSmaller(TreeNode(arr[-1]))

for i in range(n-2, -1, -1):
    ans.append(obj.insert(TreeNode(arr[i])))

l = 0
r = n-1

while l<r:
    ans[l], ans[r] = ans[r], ans[l]
    l += 1
    r -= 1

# print ans


# Find square root
def sqrt(val):
    a = val
    b = 1
    e = 0.00001

    while a-b > e:
        a = (a+b)/2.0
        b = val/a

    return a

# print sqrt(100)


# Find peak in 2D array
def find_peak(mat):
    row = len(mat)
    col = len(mat[0])
    return get_peak_helper(mat, row, col, col/2)

def get_peak_helper(mat, row, col, mid):
    mx_ele, mx_index = find_max_in_col(mat, row, mid)

    if mx_index == 0 or mx_index == col-1:
        return mx_ele

    if mat[mx_index][mid-1] <= mx_ele and mx_ele >= mat[mx_index][mid+1]:
        return mx_index

    if mx_ele < mat[mx_index][mid-1]:
        return get_peak_helper(mat, row, col, mid-ceil(mid/2))
    return get_peak_helper(mat, row, col, mid+ceil(mid/2))

def find_max_in_col(mat, row, mid):
    mx_ele, mx_index = mat[0][mid], 0
    for i in range(1, row):
        if mat[i][mid] > mx_ele:
            mx_ele, mx_index = mat[i][mid], i
    return mx_ele, mx_index

mat = [[10, 8, 10, 10],
       [14, 13, 12, 11],
       [15, 9, 11, 21],
       [16, 17, 19, 20]]

# print find_peak(mat)




# LRU

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

        def _add(self, node):
            prv = self.tail.prev
            prv.next = node
            node.prev = prv
            node.next = self.tail
            self.tail.prev = node

        def _remove(self, node):
            nxt = head.next
            nxt.prev = node
            node.next = nxt
            node.prev = self.head
            self.head.next = node

        def get(self, key):
            if self.dict.get(key):
                self._remove(self.dict.get(key))
                self._add(self.dict.get(key))
                return self.dict.get(key).val
            return -1

        def put(self, key, val):
            if self.dict.get(key):
                self._remove(self.dict.get(key))
            node = Node(key, val)
            self._add(node)
            self.dict[key] = node
            if len(self.dict) > self.capacity:
                tmp = head.next
                self._remove(tmp)
                del self.dict[tmp.key]
def custom_pow(x, y):
    res = 1
    while y>0:
        if y&1:
            res *= x
        y >>= 1
        x *= x
    return res
# print custom_pow(2, 3)

def get_height(root):
    if root is None:
        return 0
    return 1 + max(get_height(root.left), get_height(root.right))

def count_nodes_in_complete_BT(root):
    height = get_height(root)

    total_last_level_nodes = custom_pow(2, height-1)


# Maximum product of sum of two contiguous subarrays of an array
def max_sum_product(arr):
    n = len(arr)
    prefix_sum_arr = [None]*n
    prefix_sum_arr[0] = arr[0]
    for i in range(1, n):
        prefix_sum_arr[i] = arr[i] + prefix_sum_arr[i-1]

    res = 0

    for i in range(n-1):
        left_sum = prefix_sum_arr[i]
        right_sum = prefix_sum_arr[-1] - prefix_sum_arr[i]

        res = max(res, left_sum*right_sum)

    return res

arr = [4, 10, 1, 7, 2, 9]
# print max_sum_product(arr)


# Find the maximum number of subsequence from source string to form target string
# Example1: source = 'abc', target = 'abcbc' -> output: 2
# Example2: source = 'abc', target = 'acdbc' -> output: -1
def required_subsequences(source, target):

    res = 0
    while target:
        subsequence = ''
        i = 0
        j = 0
        while i < len(source) and j < len(target):
            if source[i] == target[j]:
                subsequence += target[j]
                j += 1
            i += 1
        if not len(subsequence):
            return -1

        res += 1
        target = target[len(subsequence):]

    return res

source = 'abc'
target = 'abcdbc'
# print required_subsequences(source, target)



# Product of all Subarrays of an Array
def product_of_all_subarrays(arr):
    n = len(arr)
    res = 1

    # # Time complexity - O(n^2)
    # for i in range(n):
    #     product = 1
    #     for j in range(i, n):
    #         product *= arr[j]
    #         res *= product

    # Time complexity - O(n)
    for i in range(n):
        res *= pow(arr[i], (i+1)*(n-i))
    
    return res

arr = [2, 4]
# print product_of_all_subarrays(arr)



# Binary indexed tree (BIT)
def get_query_sum(bit_arr, i):
    s = 0
    i += 1
    while i:
        s += bit_arr[i]
        i -= i&(-i)
    return s

def update(bit_arr, n, i, v):
    i += 1
    while i <= n:
        bit_arr[i] += v
        i += i&(-1)

def create(arr):
    n = len(arr)
    bit_arr = [0]*(n+1)

    for i in range(n):
        update(bit_arr, n, i, arr[i])

    return bit_arr

arr = [1, 2, 3, 4, 5]
# bit_arr = create(arr)
# print bit_arr
# print get_query_sum(bit_arr, 2)

def convert(arr):
    dct = {}
    tmp = sorted(arr)
    for i, v in enumerate(tmp):
        dct[v] = i
    for i in range(len(arr)):
        arr[i] = dct[arr[i]]

def count_inversion(arr):
    inv_count = 0
    convert(arr)
    # print arr

    n = len(arr)
    bit_arr = [0]*(n+1)
    smaller_right = [0]*n
    for i in range(n-1, -1, -1):
        print i, arr[i]
        print "BIT-before: ", bit_arr
        smaller_right[i] = get_query_sum(bit_arr, arr[i])
        inv_count += get_query_sum(bit_arr, arr[i])
        update(bit_arr, n, arr[i], 1)
        print "BIT-after: ", bit_arr
        print

    print smaller_right
    return inv_count

# arr = [3, 1, 2]
# arr = [8, 4, 2, 1]
arr = [5, 7, 3, 0, 9, 1, 4, 2]
# print count_inversion(arr)




# Segment tree
from math import log, ceil
def get_min(st_arr, ql, qr, l, r, p):
    # No overlap
    if ql > r or qr < l:
        return sys.maxint

    # Total overlap
    if ql <= l and qr >= r:
        return st_arr[p]

    m = (l+r)/2
    return min(get_min(st_arr, ql, qr, l, m, 2*p+1), get_min(st_arr, ql, qr, m+1, r, 2*p+2))

def construct_st_util(arr, st_arr, l, r, p):
    if l == r:
        st_arr[p] = arr[l]
        return
    m = (l+r)/2
    construct_st_util(arr, st_arr, l, m, 2*p+1)
    construct_st_util(arr, st_arr, m+1, r, 2*p+2)
    st_arr[p] = min(st_arr[2*p+1], st_arr[2*p+2])

def construct_segment_tree(arr, n):
    x = int(ceil(log(n, 2)))
    size = 2*pow(2, x) -1
    st_arr = [sys.maxint]*size
    construct_st_util(arr, st_arr, 0, n-1, 0)
    return st_arr

def handle_queries(st_arr, queries, n):
    for query in queries:
        res = get_min(st_arr, query[0], query[1], 0, n-1, 0)
        print "[{}, {}]--->{}".format(query[0], query[1], res)

arr = [7, 2, 3, 0, 5, 10, 3, 12, 18]
n = len(arr)

st_arr = construct_segment_tree(arr, n)
# print st
queries = [[0, 4], [4, 7], [7, 8]]
# handle_queries(st_arr, queries, n)

def fun(lst, k):
    first, second = None, None
    n = len(lst)
    i = 0
    while i < n:
        ele1 = lst[i]
        if ele1[1] == k:
            if first is None:
                first = 1
            elif second is None:
                second = 1
            else:
                first = min(first, second)
                second = 1
        elif i+1 < n:
            ele2 = lst[i+1]
            if ele1[1] + ele2[1] == k:
                if first is None:
                    first = 2
                elif second is None:
                    second = 2
                elif first != 1 and second != 1:
                    first = min(first, seconf)
                    second = 2
        i += 1

    if first is None or second is None:
        return -1
    return first+second


lst = [[0, 1], [1, 1], [2, 2], [3, 3], [4, 4], [5, 6], [6, 3], [7, 2], [8, 5], [9, 2], [10, 3]]
# print fun(lst, 5)


def f(n):
    while n:
        print n/26, n%26
        n = n/26

num = 456976
# f(num)



'''
input:  dict = {
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : {
                        "" : "1"
                    }
                }
            }
        }

output: {
            "Key1" : "1",
            "Key2.a" : "2",
            "Key2.b" : "3",
            "Key2.c.d" : "3",
            "Key2.c.e" : "1"
        }
'''
def helper(key_string, dictionary, output):      
  for k, v in dictionary.iteritems():
    if k != '':
      if key_string != '':
        k = key_string + '.' + k
      
    else:
        k = key_string
    
    if type(v) != dict:
        output[k] = v

    else:
        helper(k, v, output)

def flatten_dictionary(d):
  output = dict()
  helper('', d, output)
  return output
  

dictionary = {
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : {
                        "" : "1"
                    }
                }
            }
        }
# print(flatten_dictionary(dictionary))

def fun(arr, newBudget):
    # arr.sort(reverse=True)
    # arr.append(0)
    # surplus = sum(arr) - newBudget
    
    # if surplus <= 0:
    #     return arr[0]

    # for i in range(len(arr) - 1):
    #     surplus -= (i+1)*(arr[i] - arr[i+1])
    #     if surplus <= 0:
    #         break

    # return arr[i+1] + (-surplus)/float(i+1)

    arr.sort()
    psum = 0
    for i, g in enumerate(arr):
        remain = newBudget - psum
        tmp = g*(len(arr) - i)
        if tmp > remain:
            return (1.0*remain)/(len(arr) - i)
        psum += g

    return arr[-1]

arr = [2, 100, 50, 120, 1000]
newBudget = 190
# print fun(arr, newBudget)

