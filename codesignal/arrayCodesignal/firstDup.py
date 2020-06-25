def firstDuplicate(a):
    n = len(a)
    for i in range(n):
        val = a[i]
        arr = a[0:i]
        if val in arr:
            return val
    return -1

a = [1, 1, 2, 2, 1]
firstDuplicate(a)