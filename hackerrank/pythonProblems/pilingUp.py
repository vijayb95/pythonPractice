from collections import deque

def check(data):
    big = 0
    out = 'Yes'
    while(data):
        left = data.popleft()
        if data: right = data.pop()
        else: right = 0
        if big == 0:
            if left>=right: big = left
            else: big = right
        if left >= right and left <= big: big = left
        elif right > left and right <= big: big = right
        else: return 'No'
    return out

if __name__ == "__main__":
    for i in range(int(input())):
        int(input())
        data = deque(map(int, input().split()))
        print(check(data))