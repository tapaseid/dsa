# Given an unsorted array of size n. Array elements are in range from 1 to n.
# One number from set {1, 2,...,n} is missing and one number occurs twice in array.
# Find these two numbers.

def repeatedNumber(A):
    res = []
    for i in range(len(A)):
        if A[abs(A[i])-1] > 0:
            A[abs(A[i])-1] = -A[abs(A[i])-1]
        else:
            res.append(abs(A[i]))
    for i in range(len(A)):
        if A[i] > 0:
            res.append(i+1)
    return res

def repeated_and_missing_no(arr):
    n = len(arr)
    sum_of_squares = 0
    for i in arr:
        sum_of_squares += i*i
    a_minus_b = sum(arr) - (n*(n+1))/2
    a2_minus_b2 = sum_of_squares - (n*(n+1)*(2*n+1))/6
    a_puls_b = a2_minus_b2/a_minus_b
    a = (a_puls_b+a_minus_b)/2
    b = a_puls_b - a

    return [a, b]

A = [3, 1, 2, 5, 3]
# print repeatedNumber(A)
print repeated_and_missing_no(A)
