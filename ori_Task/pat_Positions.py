with open('C:/Users/shenme/Desktop/Bio-Informatics/ori_Task/dataset_3_5.txt') as f:
    target = "CGC"
    # f.readline().strip()
    print(target)
    text = "ATGACTTCGCTGTTACGCGC "
    # f.readline().strip()
    print(text)
    count = 0
    start = 0
    positions = []
    while start < len(text):
        pos = text.find(target, start)
        if pos != -1:
            start = pos + 1
            count += 1
            print(pos, end=" ")
            positions.append(pos)
        else:
            break

    print(positions)
