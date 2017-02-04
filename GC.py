import re

def GC(filename='rosalind_gc.txt'):
    """Computing GC Content"""
    with open(filename, 'r') as f:
        data = f.read().replace('\n', '')

    DNA = re.findall('[ATCG]+', data)
    FASTA = re.findall('>Rosalind_\d+', data)
    GC = [(i.count("G")+i.count("C"))/len(i)*100 for i in DNA]

    print(FASTA[GC.index(max(GC))])
    print(max(GC))
