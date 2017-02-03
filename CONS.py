import re

def CONS(filename='rosalind_cons.txt'):
    """Finding a Most Likely Common Ancestor"""
    listA = ['A:']
    listC = ['C:']
    listG = ['G:']
    listT = ['T:']
    best = []
    with open(filename, 'r') as f:
        data = f.read().replace('\n', '')

    DNA = re.findall('[ATCG]+', data)
    DNA = ["".join(list(y)) for y in zip(*(list(x) for x in DNA))]

    for i in DNA: listA.append(i.count('A'))
    for i in DNA: listC.append(i.count('C'))
    for i in DNA: listG.append(i.count('G'))
    for i in DNA: listT.append(i.count('T'))

    for i in range(1, len(listA)): best.append([listA[i], listC[i], listG[i], listT[i]].index(max([listA[i], listC[i], listG[i], listT[i]])))
    for i in best:
        if i == 0: print('A', end='')
        if i == 1: print('C', end='')
        if i == 2: print('G', end='')
        if i == 3: print('T', end='')
    print()
    for i in listA: print(i, end=' ')
    print()
    for i in listC: print(i, end=' ')
    print()
    for i in listG: print(i, end=' ')
    print()
    for i in listT: print(i, end=' ')
