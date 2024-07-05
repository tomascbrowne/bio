import operator
genome = ""

with open('C:/Users/shenme/Desktop/Bio-Informatics/week_2/data/dataset_7_10.txt') as f:
    genome = f.readline().strip()

genome = list(genome)
genome = "CATTCCAGTACTTCGATGATGGCGTGAAGA"
curr_skew = 0
curr_min = 0
min_vals = []
for i in range(len(genome)):
    match genome[i]:
        case "C":
            curr_skew -= 1
            min_vals.append(curr_skew)
            if curr_skew <= curr_min:
                curr_min = curr_skew
        case "G":
            curr_skew += 1
            min_vals.append(curr_skew)
        case _:
            min_vals.append(curr_skew)

for i in range(len(min_vals)):
    if min_vals[i] == curr_min:
        print(i+1, end=" ")
