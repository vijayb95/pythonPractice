def firstNotRepeatingCharacter(s):
    out = "_"
    n = len(s)
    for i in range(n):
        if s[i] in s[i+1:]:
            continue
        else:
            out = s[i]
            break
    return out

s = "abacabad"
firstNotRepeatingCharacter(s)