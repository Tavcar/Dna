# -*- coding: utf-8 -*-

hair = ["CCAGCAATCGC", "GCCAGTGCCG", "TTAGCTATCGC"]
faical_shape = ["GCCACGG", "ACCACAA", "AGGCCTCA"]
eye_colour = ["TTGTGGTGGC", "GGGAGGTGGC", "AAGTAGTGAC"]
gender = ["TGAAGGACCTTC", "TGCAGGAACTTC"]
race = ["AAAACCTCA", "CGACTACAG", "CGCGGGCCG"]

dna = open('dna.txt').read()

storilec = []

def dodaj(list, dna):
    for k in list:
         if k in dna:
                storilec.append(k)
                return k

dodaj(hair, dna)
dodaj(faical_shape, dna)
dodaj(eye_colour, dna)
dodaj(gender, dna)
dodaj(race, dna)

eva = ["TTAGCTATCGC", "AGGCCTCA", "TTGTGGTGGC", "TGAAGGACCTTC", "AAAACCTCA"]
larisa = ["GCCAGTGCCG", "AGGCCTCA", "AAGTAGTGAC", "TGAAGGACCTTC", "AAAACCTCA"]
matej = ["CCAGCAATCGC", "AGGCCTCA", "TTGTGGTGGC", "TGCAGGAACTTC", "AAAACCTCA"]
miha = ["GCCAGTGCCG", "GCCACGG", "GGGAGGTGGC", "TGCAGGAACTTC", "AAAACCTCA"]

print("DNK pripada osebi:")

if eva == storilec:
    print("Eva")

if larisa == storilec:
    print("Larisa")

if matej == storilec:
    print("Matej")

if miha == storilec:
    print("Miha")