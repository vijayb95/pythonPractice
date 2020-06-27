def isCryptSolution(crypt, solution):
    sol = dict()
    for l in solution:
        sol.update({l[0]:l[1]})
    one = ""
    two = ""
    out = ""
    for i in range(3):
        for v in crypt[i]:
            if v in sol.keys():
                if i == 0: one += sol[v]
                elif i == 1: two += sol[v]
                else: out += sol[v]
    if one[0] == '0' and len(one) > 1: return False
    if two[0] == '0' and len(two) > 1: return False
    if out[0] == '0' and len(out) > 1: return False

    if int(one) + int(two) == int(out): return True
    
    return False
    
crypt = ["WASD",
"IJKL",
"AOPAS"]
solution = [["W","2"],
["A","0"],
["S","4"],
["D","1"],
["I","5"],
["J","8"],
["K","6"],
["L","3"],
["O","7"],
["P","9"]]

isCryptSolution(crypt, solution)