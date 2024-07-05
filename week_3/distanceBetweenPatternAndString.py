import math


def hamming_distance(m_1, m_2):
    return sum(s1 != s2 for s1, s2 in zip(m_1, m_2))


def distanceBetweenPatternAndString(pattern, dna):
    k = len(pattern)
    distance = 0
    for strand in dna:
        hammingDist = k * k
        for j in range(len(strand) - k + 1):
            currHam = hamming_distance(pattern, strand[j : j + k])
            if hammingDist > currHam:
                hammingDist = currHam
        distance = distance + hammingDist
    return distance


mf = open(
    "C:/Users/shenme/Desktop/Bio-Informatics/week_3/data/dataset_5164_1.txt", "r+"
)
patt = mf.readline().strip()
dna = mf.readline().strip()
dna = dna.split(" ")

print(distanceBetweenPatternAndString(patt, dna))
