from collections import OrderedDict

def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    init = k
    ls = []
    i = 0
    
    while True:
        ls.append(string[i:k])
        i = k
        k += init
        if i == n: break
    
    for i in ls:
        print(removeDupWithOrder(i))
    
def removeDupWithOrder(a): 
    output = ""
    for x in a:
        if x not in output:
            output += x
    return output

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)