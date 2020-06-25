from collections import Counter

if __name__ == '__main__':
    
    totalShoeCount = input()
    shoes = list(map(int, input().rstrip().split()))
    customerCount = int(input())
    i = 0
    sizePrice = []
    profit = 0
    while i < customerCount:
        sizePrice.append(list(map(int, input().rstrip().split())))
        i += 1
    shoes = list(Counter(shoes).items())
    shoes = list(map(list, shoes))
    print(shoes)
    for size, price in sizePrice:
        for i in range(len(shoes)):
            if size == shoes[i][0] and shoes[i][1] > 0:
                shoes[i][1] -= 1
                profit += price
                break
    print(profit)
