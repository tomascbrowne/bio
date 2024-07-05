import math


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


def hamming_distance(m_1, m_2):
    return sum(s1 != s2 for s1, s2 in zip(m_1, m_2))


def score(motifs):
    consensus = findConsensus(motifs)
    score = 0
    for motif in motifs:
        score += hamming_distance(motif, consensus)
    return score


mf = open("C:/Users/shenme/Desktop/Bio-Informatics/week_3/data/dataset_160_9.txt", "r+")
k = mf.readline().strip()
k = k.split(" ")
t = k[1]
t = int(t)
k = k[0]
k = int(k)
dna = mf.readline().strip()
dna = dna.split(" ")

bestMotifs = []
for i in range(t):
    bestMotifs.append(dna[i][0:k])

# takes the first motif found in the first strand of DNA then constructs a profile matrix based off
# this, then computes our next based kmer by finding the most probable kmer in the DNA strand using our
# initial profile matrix
base_strand = dna[0]
remaining_strands = dna[1:t]

for j in range(len(base_strand) - k + 1):
    motifs = []
    motifs.append(base_strand[j : j + k])
    for strand in remaining_strands:
        profileMatrix = motif_probs(motifs)
        nextMotif = mostProbableKmer(strand, profileMatrix)
        motifs.append(nextMotif)
    if score(motifs) < score(bestMotifs):
        bestMotifs = motifs

# print(bestMotifs)

for motif in bestMotifs:
    print(motif, end=" ")
