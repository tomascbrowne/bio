with open('C:/Users/shenme/Desktop/Bio-Informatics/ori_Task/dataset_3_2.txt') as f:
    # strand = f.readline()
    strand = "GATTACA"
    # print(strand)
    strandArray = list(strand)
    # print(strandArray)
    # strandArray.remove('\n')
    neuclotides = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }
    output = ""

    for l in strandArray:
        output += neuclotides[l]

    print(output[::-1])
