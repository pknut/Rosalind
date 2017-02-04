def MRNA(filename="rosalind_mrna.txt"):
    """Inferring mRNA from Protein"""
    with open(filename, 'r') as f:
        data = f.read()

    rna=3
    if data.count("I"): rna*=(3**data.count("I"))%1000000
    for i in "CDEFHKNQY":
        if data.count(i): rna=(rna*2**data.count(i))%1000000
    for i  in "AGPTV":
        if data.count(i): rna=(rna*4**data.count(i))%1000000
    for i in "LRS":
        if data.count(i): rna=(rna*6**data.count(i))%1000000

    print(rna)