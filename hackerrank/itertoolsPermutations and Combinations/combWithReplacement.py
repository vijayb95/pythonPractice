from itertools import combinations_with_replacement

if __name__ == '__main__':
    
    inp = list(input().rstrip().split())
    inpString= sorted(inp[0])
    inpLength = int(inp[1])
    perm = list(combinations_with_replacement(inpString,inpLength))
    for values in perm:
        out = ''
        for v in values:
            out += v
        print(out)