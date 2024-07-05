profile = {
    "A": [],
    "C": [],
    "G": [],
    "T": [],
}

mf = open("C:/Users/shenme/Desktop/Bio-Informatics/week_3/data/dataset_159_3.txt", "r+")
string = mf.readline().strip()
k = mf.readline().strip()
k = int(k)

nucleo = ["A", "C", "G", "T"]
for i in range(4):
    nuc = mf.readline().strip()
    nuc = nuc.split(" ")
    for j in range(len(nuc)):
        nuc[j] = float(nuc[j])
    profile[nucleo[i]] = nuc

print(profile)

max_probs = 0
max_ind = 0
for j in range(len(string) - k + 1):
    kmer = string[j : j + k]
    curr = float(0)
    for i in range(len(kmer)):
        if i == 0:
            curr = profile[kmer[i]][i]
        else:
            curr *= profile[kmer[i]][i]
    if curr >= max_probs:
        max_probs = curr
        max_ind = j
print(string[max_ind : max_ind + k])
