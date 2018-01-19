# Fibonacci

def fib_rec(n):
    # Time complexity O(2^n)
    
    if n < 0:
        print "Incorrect value"
        return
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib_rec(n-1) + fib_rec(n-2)


FibArray = [0, 1]

def fibonacci(n):
    # Time complexity O(n)
    # Space complexity O(n)

    if n < 0:
        print "Incorrect value"
        return
    elif n < len(FibArray):
        return FibArray[n]
    else:
        temp = fibonacci(n-1) + fibonacci(n-2)
        FibArray.append(temp)
        return temp


def fibonacci_space_optimized(n):
    # Time complexity O(n)
    # Space complexity O(1)

    if n < 0:
        print "Incorrect value"
        return
    a = 0
    b = 1

    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return b


# x^y method of time complexity O(log y)
def power(x, y):
    res = 1
    while(y>0):
        # if y is odd multiply x with result
        if y&1:
            res = res*x
        y = y>>1 # y = y/2
        x = x*x # change x to x^2
    return res

# print power(3,5)

import math
phi = (math.sqrt(5) + 1)/2
def nth_fib_golden_ratio(n):
    if n < 0:
        print "Incorrect value"
        return
    phi_n = power(phi, n)
    return int(math.floor(phi_n/math.sqrt(5) + 1.0/2))


if __name__ == '__main__':
    print fib_rec(9)
    print fibonacci(9)
    print fibonacci_space_optimized(9)
    print nth_fib_golden_ratio(9)
