def disemvowel(string):
    string = string.replace('i'and'v',' ')
    return string
    
if __name__ == '__main__':
    s = input()
    print(disemvowel(s))