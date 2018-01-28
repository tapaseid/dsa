def printNext(arr):
    n = len(arr)
    s = []

    s.append(arr[0])
    i = 1
    while i < n:
        if s:
            if arr[i] < s[-1]:
                s.append(arr[i])
                i += 1
            else:
                print("{}--->{}".format(s.pop(), arr[i]))

        else:
            s.append(arr[i])
            i += 1

    while s:
        print("{}--->{}".format(s.pop(), -1))
if __name__ == '__main__':
    arr = [13, 7, 6, 12]
    printNext(arr)
