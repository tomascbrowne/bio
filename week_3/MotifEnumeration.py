mf = open("C:/Users/shenme/Desktop/Bio-Informatics/week_3/data/dataset_156_8.txt", "r+")
k = mf.readline().strip()
k = int(k)
d = mf.readline().strip()
d = int(d)
dna = mf.readline().strip()

dna = dna.split(" ")

patterns = dict()


def hamming_distance(a, b):
    distance = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            distance += 1
    return distance


def Neighbors(pattern, d):
    if d == 0:
        return [pattern]
    if len(pattern) == 1:
        return ["A", "C", "G", "T"]

    neighborhood = []
    suffixNeighbors = Neighbors(pattern[1:], d)
    for curr_text in suffixNeighbors:
        if hamming_distance(pattern[1:], curr_text) < d:
            neighborhood.append("A" + curr_text)
            neighborhood.append("C" + curr_text)
            neighborhood.append("G" + curr_text)
            neighborhood.append("T" + curr_text)
        else:
            neighborhood.append(pattern[0] + curr_text)

    return neighborhood


k_mer_sets = [set() for _ in dna]

print(len(k_mer_sets))
print(len(dna))

j = 0
for text in dna:
    for i in range(len(text) - k + 1):
        k_mers = Neighbors(text[i : i + k], d)
        k_mer_sets[j].update(k_mers)
    j += 1

# print(k_mer_sets)
uniq = set.intersection(*k_mer_sets)
# for j in uniq:
#     for i in range(len(k_mer_sets)):
#         if not j in k_mer_sets[i]:
#             break
#     print(j)
print(uniq)

for i in uniq:
    print(i, end=" ")

# for i in patterns:
#     if patterns[i] == max:
#         print(i)
