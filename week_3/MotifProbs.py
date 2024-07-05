import math

Motifs = [
    "TCGGGGGTTTTT",
    "CCGGTGACTTAC",
    "ACGGGGATTTTC",
    "TTGGGGACTTTT",
    "AAGGGGACTTCC",
    "TTGGGGACTTCC",
    "TCGGGGATTCAT",
    "TCGGGGATTCCT",
    "TAGGGGAACTAC",
    "TCGGGTATAACC",
]

# probs = [4][len(Motifs[0])]
probs = [[0] * len(Motifs[0]) for i in range(4)]

for j in range(len(Motifs[0])):
    for i in Motifs:
        print(i)
        match i[j]:
            case "A":
                probs[0][j] += 1
            case "T":
                probs[1][j] += 1
            case "G":
                probs[2][j] += 1
            case "C":
                probs[3][j] += 1

for i in range(len(probs[0])):
    for j in range(4):
        probs[j][i] = probs[j][i] / len(Motifs)

current_sum = 0
for i in range(len(probs[0])):
    if probs[0][i] != 0:
        current_sum += probs[0][i] * abs(math.log(probs[0][i], 2))
    if probs[1][i] != 0:
        current_sum += probs[1][i] * abs(math.log(probs[1][i], 2))
    if probs[2][i] != 0:
        current_sum += probs[2][i] * abs(math.log(probs[2][i], 2))
    if probs[3][i] != 0:
        current_sum += probs[3][i] * abs(math.log(probs[3][i], 2))


print(round(current_sum, 4))
