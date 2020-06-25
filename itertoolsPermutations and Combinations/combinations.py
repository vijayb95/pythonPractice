from itertools import combinations

if __name__ == '__main__':
    inp = list(input().rstrip().split())
    
    inpString= sorted(inp[0])
    inpLength = int(inp[1])
    
    for i in range(inpLength):
        comb = list(combinations(inpString,i+1))
        for values in comb:
            out = ''
            for v in values:
                out += v
            print(out)