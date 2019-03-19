def to_rna(dna_strand):
    lst = list(dna_strand)
    for idx,val in enumerate(lst):
        print(val)
        if val == "C":
            lst[idx] = 'G'
            print(lst[idx])
        if val == 'G':
            lst[idx] = 'C'
            print(lst[idx])
        if val == 'T':
            lst[idx] = 'A'
            print(lst[idx])
        if val == 'A':
            lst[idx] = 'U'
            print(lst[idx])
        dna_strand = ''.join(lst)
    return dna_strand


