from collections import Counter

givenList = []
uniqueList = dict()
for _ in range(int(input())):
    inp = input()
    givenList.append(inp)
    uniqueList[inp] = None #adding inputs as a key to dictionary because dictionary key cannot be duplicate and assigning value to each key as none

print(len(uniqueList))

d = Counter(givenList) #initializing counter

for i in uniqueList.keys():
    print(d[i], end=' ') #finding the number of occurences of current i
    
# sampleInput:
#     4
#     bcdef
#     abcdefg
#     bcde
#     bcdef
# sampleOutput:
#     3
#     2 1 1