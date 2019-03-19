import re


def proteins(strands):
    STRANDS = {"AUG": "Methionine",
               "UUU": "Phenylalanine",
               "UUC": "Phenylalanine",
               "UUA": "Leucine",
               "UUG": "Leucine",
               "UCU": "Serine",
               "UCC": "Serine",
               "UCA": "Serine",
               "UCG": "Serine",
               "UAU": "Tyrosine",
               "UAC": "Tyrosine",
               "UGU": "Cysteine",
               "UGC": "Cysteine",
               "UGG": "Tryptophan",
               }
    ret = []
    split_strands = re.findall(".{1,3}", strands)
    for strand in split_strands:
        if strand == "UAA" or strand == "UAG" or strand == "UGA":
            return ret
        protein = STRANDS[strand]
        ret.append(protein)
        if strand == split_strands[-1]:
            return ret
