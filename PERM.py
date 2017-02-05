import itertools

def PERM(n=3):
    """Enumerating Gene Orders"""
    l = [i for i in range(1, n+1)]
    permutation = list(itertools.permutations(l))

    print (len(permutation))

    for i in permutation:
        for j in i:
            print(j, end=" ")
        print()