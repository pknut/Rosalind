def REVC(filename='rosalind_revc.txt'):
    '''Complementing a Strand of DNA'''
    with open(filename, 'r') as f:
        print(f.read().replace("T", "U")[::-1])