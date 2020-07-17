if __name__ == '__main__':
    inp = str(input())
    
    first = inp[0]
    count = 1
    out = []
    for s in inp[1:]:
        second = s
        if first == second:
            count += 1
        else:
            v = (count, int(first))
            print(v)
            count = 1
            first = s
    v = (count, int(first))
    print(v)