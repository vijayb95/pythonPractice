# Enter your code here. Read input from STDIN. Print output to STDOUT
sizes = list(map(int, input().rstrip().split()))

listValues = list(map(int, input().rstrip().split()))

a = set(map(int, input().rstrip().split()))

b = set(map(int, input().rstrip().split()))

happiness = 0

for i in a:
    if i in listValues:
        happiness += 1
for i in b:
    if i in listValues:
        happiness -= 1

print (happiness)