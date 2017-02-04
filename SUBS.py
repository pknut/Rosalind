def SUBS(filename='rosalind_subs.txt'):
    """Finding a Motif in DNA"""
    with open(filename, 'r') as f:
        string = f.readline()[:-1]
        substring = f.readline()[:-1]

    for i in range(len(string) - len(substring)):
        if string[i:i+len(substring)] == substring: print (i+1, end=' ')
