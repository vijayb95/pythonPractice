n = int(input())
s = set(map(int, input().split())) #taking multiple space separated inputs and storing them in a set s

for _ in range(int(input())):
    cm = list(map(str,input().split()))
    if cm[0] == 'pop':
        s.pop()
    elif cm[0] == 'remove':
        s.remove(int(cm[1]))
    elif cm[0] == 'discard':
        s.discard(int(cm[1]))
        
sum = 0

for i in s:
    sum += i

print(sum)