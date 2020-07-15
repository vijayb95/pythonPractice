from collections import namedtuple

# Finally haven't used named tuple in this problem :(

t = int(input())

col = list(map(str, input().split()))
mark = 0

for i in range(t):
    values = list(map(str, input().split()))
    for j in range(len(col)):
        if col[j] == 'MARKS':
            mark += values[j]

out = mark / t

print(out)