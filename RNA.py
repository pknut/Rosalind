def RNA(filename='rosalind_dna.txt'):
    '''Transcribing DNA into RNA'''
    with open(filename, 'r') as f:
        print(f.read().replace("T", "U"))