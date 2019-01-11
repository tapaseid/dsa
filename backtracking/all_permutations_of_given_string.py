# Write a program to print all distinct permutations of a given string

def _permute(a, l, r):
    if l == r:
        print toString(a)

    else:
        for i in range(l, r+1):
            if shouldSwap(a, l, i): # check for repeated characters.
                a[l], a[i] = a[i], a[l]
                _permute(a, l+1, r)
                a[l], a[i] = a[i], a[l] # backtrack

def toString(lst):
    return "".join(lst)

def shouldSwap(a, l, curr):
    for j in range(l, curr):
        if a[curr] == a[j]:
            return 0
    return 1

def print_all_permutations(string):
    # Time complexity O(n*n!)

    n = len(string)
    a = list(string)
    _permute(a, 0, n-1)

if __name__ == '__main__':
    string = "AABC"
    # print_all_permutations(string)


################ simplest solution ##################
# B ['C']
# Result:  set(['CB', 'BC'])
# A set(['CB', 'BC'])
# Result:  set(['ACB', 'CBA', 'BCA', 'ABC', 'BAC', 'CAB'])
# set(['ACB', 'CBA', 'BCA', 'ABC', 'BAC', 'CAB'])

def permutations(word):
    if len(word) == 1:
        return [word]

    perms = permutations(word[1:])
    char = word[0]
    # print char, perms
    result = set()
    for perm in perms:
        for i in range(len(perm)+1):
            result.add(perm[:i]+char+perm[i:])
    # print "Result: ", result
    return result

print permutations('ABC')
# print permutations('ABCA')
#############################################

# Related examples:
#------------------

# Print all possible combinations of r elements in a given array of size n.

def combinationsUtil(arr, data, start, end, index, r):
    if index == r:
        print_util(data)
        return

    i = start
    while i < end:
        if end-i+1 >= r-index:
            data[index] = arr[i]
            combinationsUtil(arr, data, i+1, end, index+1, r)

        i += 1

        # Remove duplicates
        while i < end and arr[i] == arr[i-1]:
            i += 1

def combinationsUtil_recursion(arr, data, start, end, index, r):
    # Not handled for duplicates.

    if index == r:
        print_util(data)
        return

    if start >= end:
        return

    # current is included, put next at next location
    data[index] = arr[start]
    combinationsUtil(arr, data, start+1, end, index+1, r)

    # current is excluded, replace it with next (i+1 is passed, but index is not changed)
    combinationsUtil(arr, data, start+1, end, index, r)

def print_util(data):
    for i in data:
        print i,
    print

def printCombinations(arr, n, r):

    data = [None]*r
    # combinationsUtil_recursion(arr, data, 0, n, 0, r)
    print "Another....."
    list.sort(arr)
    combinationsUtil(arr, data, 0, n, 0, r)

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 1]
    n = len(arr)
    r = 3
    printCombinations(arr, n, r)
