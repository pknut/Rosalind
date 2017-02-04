def HAMM(filename='rosalind_hamm.txt'):
    """Counting Point Mutations"""
    with open(filename, 'r') as f:
        s = f.readline()
        t = f.readline()

    distance = 0
    for i in range(len(s)):
        if s[i] != t[i]: distance += 1

    print(distance)