import re


for _ in range(int(input())):
    reg = input()
    try:
        re.compile(reg)
        print(True)
    except:
        print(False)