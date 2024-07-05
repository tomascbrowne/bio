import math
import random


def motif_probs(Motifs):
    probs = [[1] * len(Motifs[0]) for i in range(4)]

    for j in range(len(Motifs[0])):
        for i in Motifs:
            match i[j]:
                case "A":
                    probs[0][j] += 1
                case "C":
                    probs[1][j] += 1
                case "G":
                    probs[2][j] += 1
                case "T":
                    probs[3][j] += 1

    for i in range(len(probs[0])):
        for j in range(4):
            probs[j][i] = float(probs[j][i] / len(Motifs))
    profile = {"A": probs[0], "C": probs[1], "G": probs[2], "T": probs[3]}
    return profile


def mostProbableKmer(string, profileMatrix):
    max_probs = 0
    max_ind = 0

    for j in range(len(string) - k + 1):
        kmer = string[j : j + k]
        curr = float(0)
        for i in range(len(kmer)):
            if i == 0:
                curr = profileMatrix[kmer[i]][i]
            else:
                curr *= profileMatrix[kmer[i]][i]
        if curr >= max_probs:
            max_probs = curr
            max_ind = j

    return string[max_ind : max_ind + k]


def hamming_distance(m_1, m_2):
    return sum(s1 != s2 for s1, s2 in zip(m_1, m_2))


def score(motifs):
    consensus = findConsensus(motifs)
    score = 0
    for motif in motifs:
        score += hamming_distance(motif, consensus)
    return score


def findConsensus(Motifs):
    probs = [[0] * len(Motifs[0]) for i in range(4)]
    output = ""

    for i in range(len(Motifs[0])):
        output += "A"

    for j in range(len(Motifs[0])):
        for i in Motifs:
            match i[j]:
                case "A":
                    probs[0][j] += 1
                case "C":
                    probs[1][j] += 1
                case "G":
                    probs[2][j] += 1
                case "T":
                    probs[3][j] += 1

    output = list(output)
    for j in range(len(Motifs[0])):
        max = 0
        for i in range(4):
            if probs[i][j] > max:
                max = probs[i][j]
                match i:
                    case 0:
                        output[j] = "A"
                    case 1:
                        output[j] = "C"
                    case 2:
                        output[j] = "G"
                    case 3:
                        output[j] = "T"
    return "".join(output)


def Motifs(Dna, k, profile, t):
    motifs = []
    for i in range(t):
        motifs.append(mostProbableKmer(Dna[i], profile))
    return motifs


def RandomizedMotifSearch(Dna, k, t):
    bestMotifs = []
    motifs = []
    for i in range(t):
        x = random.randrange(0, len(Dna[0]) - k + 1)
        motifs.append(Dna[i][x : x + k])
    bestMotifs = motifs
    while 1 > 0:
        profile = motif_probs(motifs)
        motifs = Motifs(Dna, k, profile, t)
        if score(motifs) < score(bestMotifs):
            bestMotifs = motifs
        else:
            return [bestMotifs, score(bestMotifs)]


mf = open("C:/Users/shenme/Desktop/Bio-Informatics/week_4/data/resr_motifs.txt", "r+")
k = mf.readline().strip()
k = k.split(" ")
t = k[1]
t = int(t)
k = k[0]
k = int(k)
dna = mf.readline().strip()
dna = dna.split(" ")

results = []
min_score = k * len(dna)
curr_min_ind = 0
for i in range(1000):
    results.append(RandomizedMotifSearch(dna, k, t))
    if results[i][1] < min_score:
        min_score = results[i][1]
        curr_min_ind = i

for i in range(len(results[0][0])):
    print(results[curr_min_ind][0][i], end=" ")
