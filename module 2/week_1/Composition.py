mf = open(
    "C:/Users/shenme/Desktop/Bio-Informatics/module 2/week_1/data/dataset_197_3.txt",
    "r+",
)
k = mf.readline().strip()
k = int(k)
dna = mf.readline().strip()

output = []
for i in range(len(dna) - k + 1):
    output.append(dna[i : i + k])

out = open(
    "C:/Users/shenme/Desktop/Bio-Informatics/module 2/week_1/data/output.txt",
    "w+",
)

for i in output:
    out.write(i)
    out.write(" ")
