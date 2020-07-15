from collections import OrderedDict

oList = OrderedDict()

for _ in range(int(input())):
    item, price = input().rsplit(" ", maxsplit=1) #splits from the right side and restricting the number of split to 1
    if item in oList:
        oList[item] += int(price)
    else:
        oList[item] = int(price)

for i in oList:
    print(i, oList[i])