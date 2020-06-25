from itertools import permutations, combinations, combinations_with_replacement, permutations_with_repetition

if __name__ == '__main__':
    perm = list(permutations([1, 2, 3, 4],2))
    perm2 = list(permutations_with_repetition([1, 2, 3, 4],2))
    comb = list(combinations([1, 2, 3, 4],2))
    comb2 = list(combinations_with_replacement([1, 2, 3, 4],2))
    print(perm)
    print(perm2)
    print(comb2)
    print(comb)