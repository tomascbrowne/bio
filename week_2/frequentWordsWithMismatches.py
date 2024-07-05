patterns = []
freqMap = dict()
n = ""

k = 5
# d = 2

text = "AGAAAGAATAGCAGAAAAAATAGCAAAAAAAAAAACAGAACTATAGCAAACAAACCTATAGCAAAAAAACAAAAAAACAGAAAGAAAAAAAGAATAGCTAGCAGAAAAAACTACTAAAAACTACTACTAAGAAAGAAAAAACTATAGCAAAAAAACCTACTAAAACCTAAAAAAAACCTAAAAAAGAAAAACAAACAAAAAAACTAGCAAACTAGCAAAACTAAGAAAAACAAAATAGCTAGCAGAAAAACTAGCAGAACTAAAACAAACAAAAAAACTAGCAGAAAGAAAAAAAAACAAACTAGCTAGCAGAAAAAATAGCAGAAAGAAAGAACTAAAAATAGC"


def hamming_distance(a, b):
    distance = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            distance += 1
    return distance


def Neighbors(pattern, d):

    # assert (d <= len(pattern))

    if d == 0:
        return [pattern]
    if len(pattern) == 1:
        return ["A", "C", "G", "T"]

    neighborhood = []
    suffixNeighbors = Neighbors(pattern[1:], d)
    # print(suffixNeighbors)
    for curr_text in suffixNeighbors:
        if hamming_distance(pattern[1:], curr_text) < d:
            neighborhood.append("A" + curr_text)
            neighborhood.append("C" + curr_text)
            neighborhood.append("G" + curr_text)
            neighborhood.append("T" + curr_text)
        else:
            neighborhood.append(pattern[0] + curr_text)

    return neighborhood


for i in range(len(text) - k):
    pattern = text[i:i+k]
    neighborhood = Neighbors(pattern, 3)
    for j in neighborhood:
        if j in freqMap.keys():
            freqMap[j] += 1
        else:
            freqMap[j] = 1

max = max(freqMap.values())

print(max)

with open('C:/Users/shenme/Desktop/Bio-Informatics/week_2/data/output', 'w') as f:
    for i in freqMap:
        if freqMap[i] == max:
            f.write(i)
            f.write(' ')
