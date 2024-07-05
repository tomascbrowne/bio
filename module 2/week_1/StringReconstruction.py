mf = open(
    "C:/Users/shenme/Desktop/Bio-Informatics/module 2/week_1/data/dataset_198_3.txt",
    "r+",
)

dna = mf.readline().strip()
dna = dna.strip("\n")
dna = dna.split(" ")

output = dna[0]

for i in range(0, len(dna)):
    count = 0
    while count != len(dna[i]):
        check = True
        if dna[i - 1][count] == dna[i][0]:
            for j in range(len(dna[i][count : len(dna[i])])):
                if dna[i][j + count] != dna[i - 1][j + count]:
                    check = False
        if check == True:
            break
        count += 1

    output = output[0 : len(output) - len(dna[0]) + count] + dna[i]

print(output)

patts = dna


def combine(string, patterns):
    for patt in patterns:
        if string[len(string) - len(patt) + 1 :] == patt[:-1]:
            string += patt[-1]
    return string


def PathToGenome(patts):
    string = ""
    string += patts[0]
    Genome = combine(string, patts[1:])
    return Genome


print(PathToGenome(patts))

# while the finally value of the firs tsring does match the first of
