def DNA(filename='rosalind_dna.txt'):
    '''Counting DNA Nucleotides'''
    with open(filename, 'r') as f:
        data=f.read()

    for i in "ACGT": print(data.count(i), end=" ")
