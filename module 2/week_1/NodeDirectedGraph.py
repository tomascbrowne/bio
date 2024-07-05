mf = open(
    "C:/Users/shenme/Desktop/Bio-Informatics/module 2/week_1/data/dataset_198_3.txt",
    "r+",
)

nodes = {}

dna = mf.readline().strip()
dna = dna.strip("\n")
dna = dna.split(" ")

for patt in dna:
    for otherPatt in dna:
        if otherPatt != patt:
            for i in range(len(patt)):
                if patt[i:] == otherPatt[:-i]:
                    if nodes[patt] == None:
                        nodes[patt] = otherPatt
                    else:
                        nodes[patt] += " " + otherPatt

for patt in dna:
    print(patt + ": " + nodes[patt])
