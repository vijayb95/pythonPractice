def minion_game(string):
    # your code goes here
    Stuart = 0
    Kevin = 0
    vowels = 'AEIOU'
    for i in range(len(string)):
        if string[i] in vowels : Kevin += (len(string)-i)
        else : Stuart += (len(string)-i)
                
    if Stuart > Kevin : print(f"Stuart {Stuart}")
    elif Stuart < Kevin : print(f"Kevin {Kevin}")
    else : print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)