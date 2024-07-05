import itertools


def hamming_distance(m_1, m_2):
    return sum(s1 != s2 for s1, s2 in zip(m_1, m_2))


mf = open(
    "C:/Users/shenme/Desktop/Bio-Informatics/week_3/data/medianStringsData.txt", "r+"
)
k = mf.readline().strip()
k = int(k)
dna = mf.readline().strip()
dnas = dna.split(" ")
patterns = ["".join(i) for i in itertools.permutations("ACTG", k)]
output_patterns = {}

# for i in range(len(dnas[0]) - k + 1):
#     patterns.append(dnas[0][i : i + k])

# print(dnas)
# print(patterns)

# for j in range(len(patterns)):
#     for string in dnas:
#         distance = None
#         min_distance = None
#         min_kmer_loc = None
#         total_dist = 0
#         for i in range(len(dnas[0]) - k + 1):
#             if i == 0:
#                 min_distance = hamming_distance(patterns[j], string[i:k])
#                 min_kmer_loc = i
#             else:
#                 distance = hamming_distance(patterns[j], string[i : i + k])
#                 if min_distance > distance:
#                     min_distance = distance
#                     min_kmer_loc = i
#         total_dist += min_distance
#     output_patterns[patterns[j]] = total_dist

# lowest_dist = k * len(dnas)
# out = ""
# for key in output_patterns:
#     if output_patterns[key] < lowest_dist:
#         lowest_dist = output_patterns[key]
#         out = key

# for items in out:
#     print(items, end=" ")


def distanceBetweenPatNString(pattern, Dna):
    distance = 0
    for string in Dna:
        hamming_dist = k * len(Dna)
        for i in range(len(string) + 1 - k):
            curr = hamming_distance(pattern, string[i : i + k])
            if hamming_dist >= curr:
                hamming_dist = curr
        distance = distance + hamming_dist
    return distance


def medianString(Dna, k):
    distance = k * len(dnas)
    median = ""
    for j in range(len(patterns)):
        pattern = patterns[j]
        curr = distanceBetweenPatNString(pattern, Dna)
        if distance >= curr:
            distance = curr
            median = pattern
    return median


print(patterns)
print(medianString(dnas, k))
