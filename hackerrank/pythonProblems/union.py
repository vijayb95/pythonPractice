enSet = set()
frSet = set()

en = input()
enList = list(map(int,input().split()))

fr = input()
frList = list(map(int,input().split()))

for i in enList:
    enSet.add(i)
for i in frList:
    frSet.add(i)

total = enSet.union(frSet)

print(len(total))