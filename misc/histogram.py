# Find the largest rectangular area possible in a given histogram where the
# largest rectangle can be made of a number of contiguous bars.
# For simplicity, assume that all bars have same width and the width is 1 unit.



# Time complexity O(n)
def largest_rectangle(hist, n):
    s = []
    max_area = 0
    i = 0
    while i < n:
        if not s:
            s.append(i)
            i += 1
        
        else:
            if hist[s[-1]] <= hist[i]:
                s.append(i)
                i += 1
            else:
                tp = s.pop()
                curr_area = hist[tp]*(i-s[-1]-1 if s else i)
                if max_area < curr_area:
                    max_area = curr_area
    while s:
        tp = s.pop()
        curr_area = hist[tp]*(i-s[-1]-1 if s else i)
        if max_area < curr_area:
            max_area = curr_area

    return max_area


def constructSTUtil(hist, st, low, high, pos):
    if low == high:
        st[pos] = low
        return
    mid = (low+high)/2
    constructSTUtil(hist, st, low, mid, 2*pos+1)
    constructSTUtil(hist, st, mid+1, high, 2*pos+2)
    st[pos] = minVal(hist, st[2*pos+1], st[2*pos+2])

def constructST(hist, n):
    from math import log, ceil
    x = int(ceil(log(n, 2)))
    max_size = 2*pow(2, x) - 1
    st = [None]*max_size
    constructSTUtil(hist, st, 0, n-1, 0)
    return st

def RMQUtil(hist, st, ss, se, qs, qe, pos):
    if qs <= ss and qe >= se: # Total overlap
        return st[pos]

    if qs > se or qe < ss: # No overlap
        return -1

    mid = (ss+se)/2
    return minVal(hist, RMQUtil(hist, st, ss, mid, qs, qe, 2*pos+1),
        RMQUtil(hist, st, mid+1, se, qs, qe, 2*pos+2))

def RMQ(hist, st, n, l, r):

    # #Naive approach, not interested
    # min_index = l
    # for i in range(l, r):
    #     if hist[i] < hist[min_index]:
    #         min_index = i

    # return min_index

    return RMQUtil(hist, st, 0, n-1, l, r, 0)

def getMaxArea(hist, st, n, l, r):


    # Base case
    if l > r: return -1
    if l == r: return hist[l]

    # Find index of the minimum value in given range
    # This will take O(log n)
    min_index = RMQ(hist, st, n, l, r)

    return max(getMaxArea(hist, st, n, l, min_index),
        getMaxArea(hist, st, n, min_index+1, r), (r-l+1)*hist[min_index])

def minVal(hist, i, j):
    return i if hist[i] < hist[j] else j

# Divide and conquer method
# Range Minimum Query using Segment Tree
# T(n) = O(Log n) + T(n-1)
# Overall time complexity O(nLogn)
def largest_rectangle_RMQ(hist, n):
    
    # Build segment tree from given array in O(n) time
    st = constructST(hist, n)
    # print st

    # Use recursive utility function to get maximum area
    return getMaxArea(hist, st, n, 0, n-1)

if __name__ == '__main__':
    hist = [1, 2, 3, 4]
    # hist = [6, 2, 5, 4, 5, 1, 6]
    # print largest_rectangle(hist, len(hist))
    print largest_rectangle_RMQ(hist, len(hist))
 