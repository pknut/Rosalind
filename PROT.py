import re

def PROT(filename='rosalind_prot.txt'):
    """Translating DNA into Protein"""
    with open(filename, 'r') as f:
        data = f.read()

    codons = re.findall("[ACGU]{3}", data)
    codons = ["A" if i in ["GCU", "GCC", "GCA", "GCG"] else i for i in codons]
    codons = ["C" if i in ["UGU", "UGC"] else i for i in codons]
    codons = ["D" if i in ["GAU", "GAC"] else i for i in codons]
    codons = ["E" if i in ["GAA", "GAG"] else i for i in codons]
    codons = ["F" if i in ["UUU", "UUC"] else i for i in codons]
    codons = ["G" if i in ["GGU", "GGC", "GGA", "GGG"] else i for i in codons]
    codons = ["H" if i in ["CAU", "CAC"] else i for i in codons]
    codons = ["I" if i in ["AUU", "AUC", "AUA"] else i for i in codons]
    codons = ["K" if i in ["AAA", "AAG"] else i for i in codons]
    codons = ["L" if i in ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"] else i for i in codons]
    codons = ["M" if i == "AUG" else i for i in codons]
    codons = ["N" if i in ["AAU", "AAC"] else i for i in codons]
    codons = ["P" if i in ["CCU", "CCC", "CCA", "CCG"] else i for i in codons]
    codons = ["Q" if i in ["CAA", "CAG"] else i for i in codons]
    codons = ["R" if i in ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"] else i for i in codons]
    codons = ["S" if i in ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"] else i for i in codons]
    codons = ["T" if i in ["ACU", "ACC", "ACA", "ACG"] else i for i in codons]
    codons = ["V" if i in ["GUU", "GUC", "GUA", "GUsG"] else i for i in codons]
    codons = ["W" if i == "UGG" else i for i in codons]
    codons = ["Y" if i in ["UAU", "UAC"] else i for i in codons]
    codons = [" " if i in ["UAA", "UAG", "UGA"] else i for i in codons]

    for i in codons: print(i, end="")