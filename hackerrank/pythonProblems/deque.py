from collections import deque

d = deque()

for _ in range(int(input())):
    eval('d.{0}({1})'.format(*input().split()+['']))
    
for _ in range(len(d)):
    print(d.popleft(), end = ' ') # can't iterate the deque normally, so popping every single value to print one after the another.
    
# sample input - 
# 6
# append 1
# append 2
# append 3
# appendleft 4
# pop
# popleft