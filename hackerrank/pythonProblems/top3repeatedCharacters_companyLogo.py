from collections import OrderedDict

if __name__ == '__main__':
    s = input()
    d = dict()
    
    for i in s:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    dic = OrderedDict(sorted(d.items(), key=lambda t: t[0]))
    dic = sorted(dic.items(), key=lambda t: t[1], reverse = True)
    
    for i in dic[0:3]:
        print(i[0], i[1])