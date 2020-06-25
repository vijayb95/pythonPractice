def rotateImage(a):
    n = len(a)
    newList = []
    for i in range(n):
        inL = []
        for j in range(n):
            inL.insert(0,a[j][i])
        newList.append(inL)
    return newList

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

rotateImage(a)