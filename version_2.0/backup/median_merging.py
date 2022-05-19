
# Merge arrays
from Queue import PriorityQueue
# q = PriorityQueue()
# print q.qsize()
# q.put((3, 10))
# q.put((2, 12))
# q.put((4, 5))
# print q.get()
# print q.get()

def mergeKArrays(arrays):
    q = PriorityQueue()
    for i in range(len(arrays)):
        q.put((arrays[i][0], i, 0))

    res = []
    while q.qsize():
        val, arr_no, index = q.get()
        res.append(val)
        if index+1 < len(arrays[arr_no]):
            q.put((arrays[arr_no][index+1], arr_no, index+1))

    return res



a1 = [1, 4, 5]
a2 = [1, 3, 4]
a3 = [2, 6]
arrays = [a1, a2, a3]

# print mergeKArrays(arrays)


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
def mergeKLists(lists):
    q = PriorityQueue()
    for i in range(len(lists)):
        if lists[i]:
            node = lists[i].next
            val = node.val
            q.put((val, node))
        
    head = curr = ListNode(0)
    while q.qsize():
        val, node = q.get()
        curr.next = ListNode(val)
        curr = curr.next
        node = node.next
        if node:
            q.put((node.val, node))
    
    print_list(head.next)
    return head


import heapq
class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists2(self, A):
        pq = []
        for h in A:
            if h:
                heapq.heappush(pq, [h.val, h])
        
        head = curr = ListNode(None)
        while pq:
            _, node = heapq.heappop(pq)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(pq, [node.next.val, node.next])
        
        return head.next


# def mergeKLists(self, lists):
#         """
#         :type lists: List[ListNode]
#         :rtype: ListNode
#         """
#         # lst = lists[0]
#         # while lst:
#         #     print lst.val
#         #     lst = lst.next
#         def heapify(arr, i, n):
#             left_child = 2*i+1
#             right_child = 2*i+2
#             shortest = i
#             if left_child < n and arr[left_child][0].val < arr[shortest][0].val:
#                 shortest = left_child
#             if right_child < n and arr[right_child][0].val < arr[shortest][0].val:
#                 shortest = right_child
                
#             if shortest != i:
#                 arr[i], arr[shortest] = arr[shortest] ,arr[i]
#                 heapify(arr, shortest, n)
                
#         arr = []
#         for i in range(len(lists)):
#             if lists[i]:
#                 arr.append([lists[i], i])
        
#         for i in range(len(arr)/2):
#             heapify(arr, i, len(arr))
            
#         head = curr = ListNode()
#         print len(arr)
#         while arr:
#             node, list_no = arr.pop(0)
#             curr.next = node
#             curr = node
#             if node.next is not None:
#                 arr.insert(0, [node.next, list_no])
#             heapify(arr, 0, len(arr))
        
#         return head.next

def make_list(arr, head):
    curr = head
    for i in arr:
        node = ListNode(i)
        curr.next = node
        curr = node

def print_list(head):
    while head is not None:
        print head.val
        head = head.next

l1 = ListNode()
l2 = ListNode()
l3 = ListNode()
a1 = [1, 4, 5]
a2 = [1, 3, 4]
a3 = [2, 6]

make_list(a1, l1)
# print_list(l1.next)
make_list(a2, l2)
# print_list(l2.next)
make_list(a3, l3)
# print_list(l3.next)

lists = [l1, l2, l3]

# head = mergeKLists(lists)



# Median of stream of integers
from heapq import heappush, heappop
class Stream:
    def __init__(self):
        self.median = None
        self.min_heap = []
        self.max_heap = []

    def median_stream(self, arr):
        self.max_heap.append(-arr[0])
        self.median = arr[0]
        print self.max_heap, self.min_heap
        print "Median: ", self.median
        
        for i in range(1, len(arr)):
            if arr[i] < self.median:
                if len(self.max_heap) == len(self.min_heap):
                    heappush(self.max_heap, -arr[i])
                else:
                    tmp = heappop(self.max_heap)
                    heappush(self.min_heap, -tmp)
                    heappush(self.max_heap, -arr[i])
            else:
                if len(self.max_heap) == len(self.min_heap):
                    tmp = heappop(self.min_heap)
                    heappush(self.min_heap, arr[i])
                    heappush(self.max_heap, -tmp)
                else:
                    heappush(self.min_heap, arr[i])
            
            if len(self.max_heap) == len(self.min_heap):
                self.median = (self.min_heap[0] - self.max_heap[0])/2.0
            else:
                self.median = - self.max_heap[0]

            print self.max_heap, self.min_heap
            print "Median: ", self.median


arr = [5, 15, 10, 20, 3]
obj = Stream()
obj.median_stream(arr)

# --------------------------------------------------------------
class MedianFinder(object):
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num):
        heapq.heappush(self.min_heap, -1*num)
        if self.min_heap and self.max_heap and -1*self.min_heap[0] > self.max_heap[0]:
            val = -1*heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, val)
        
        if len(self.min_heap) > len(self.max_heap) + 1:
            val = -1*heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, val)
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -1*val)
            
    def findMedian(self):
        if len(self.min_heap) > len(self.max_heap):
            return -1*self.min_heap[0]
        if len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0]
        return (-1*self.min_heap[0] + self.max_heap[0]) / 2.0

# ----------------------------------------------------------------

# Median of two arrays
def findMedianSortedArrays(nums1, nums2):
        
        n1 = len(nums1)
        n2 = len(nums2)
        
        if n1 > n2:
            n1, n2 = n2, n1
            nums1, nums2 = nums2, nums1
            
        if n1 == 0 and n2 == 0:
            return 0
        is_odd = (n1+n2)%2
        if n1 == 0:
            if is_odd:
                return nums2[n2/2]
            else:
                return (nums[n2/2-1]+nums2[n2/2])/2.0
        
        start = 0
        end = n1
        import sys
        while start <= end:
            x = (start+end)/2
            y = (n1+n2+1)/2 - x
            ax = nums1[x-1] if x-1 >= 0 else -sys.maxint
            axplus1 = nums1[x] if x < n1 else sys.maxint
            by = nums2[y-1] if y-1 >= 0 else -sys.maxint
            byplus1 = nums2[y] if y < n2 else sys.maxint
            
            if ax <= byplus1 and by <= axplus1:
                if is_odd:
                    return max(ax, by)
                else:
                    return (max(ax, by) + min(axplus1, byplus1))/2.0
            elif ax > byplus1:
                end = x-1
            else:
                start = x+1

arr1 = [1, 3]
arr2 = [2]

# print findMedianSortedArrays(arr1, arr2)



# class Solution(object):
#     def trapRainWater(self, heightMap):
#         """
#         :type heightMap: List[List[int]]
#         :rtype: int
#         """
#         res = 0
        
#         row = len(heightMap)
#         col = len(heightMap[0])
        
#         for r in range(row):
#             L, R = self._helper(heightMap, r, row, col)
#             for c in range(col):
#                 D, U = self._helper2(heightMap, c, row, col)
#                 print "L: ", L
#                 print "R: ", R
#                 print "D: ", D
#                 print "U: ", U
#                 print r, c
#                 tmp= min(L[c], R[c], D[r], U[r])-heightMap[r][c]
#                 print "tmp: ", tmp
#                 if tmp>0:
#                   res += tmp

#         return res
                      
#     def _helper(self, mat, r, row, col):
#             L = [None]*col
#             R = [None]*col
            
#             L[0] = mat[r][0]
#             for i in range(1, col):
#                 L[i] = max(L[i-1], mat[r][i])
            
#             R[-1] = mat[r][-1]
#             for i in range(col-2, -1, -1):
#                 R[i] = max(R[i+1], mat[r][i])
                
#             return L, R
        
#     def _helper2(self, mat, c, row, col):
#             D = [None]*row
#             U = [None]*row
            
#             D[0] = mat[0][c]
#             for j in range(1, row):
#                 D[j] = max(D[j-1], mat[j][c])
            
#             U[-1] = mat[-1][c]
#             for j in range(row-2, -1, -1):
#                 U[j] = max(U[j+1], mat[j][c])
                
#             return D, U


# mat = [   [1,4,3,1,3,2],
#           [3,2,1,3,2,4],
#           [2,3,3,2,3,1]]

# mat2 = [[12,13,1,12],
#       [13,4,13,12],
#       [13,8,10,12],
#       [12,13,12,12],
#       [13,13,13,13]]

# obj = Solution()
# print obj.trapRainWater(mat2)
















