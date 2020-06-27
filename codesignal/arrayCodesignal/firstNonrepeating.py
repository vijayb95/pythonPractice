def firstNotRepeatingCharacter(s):
    out = "_"
    n = len(s)
    a = set()
    for i in range(n):
        if s[i] in s[i+1:]:
            a.add(s[i])
            continue
        elif s[i] in a:
            continue
        else:
            out = s[i]
            break
    return out

s = "abacabad"
firstNotRepeatingCharacter(s)