# Enter your code here. Read input from STDIN. Print output to STDOUT
import os
import sys

a = input()
a_set = set(map(int, input().rstrip().split()))

b = input()
b_set = set(map(int, input().rstrip().split()))

a_set = set(a_arr)
b_set = set(b_arr)

common = a_set.intersection(b_set)

new_set = a_set.union(b_set)

for i in common:
    new_set.remove(i)

# new_list = list(new_set)
# new_list = sorted(new_list)

new_set = sorted(new_set)
for i in new_list:
    print(i)