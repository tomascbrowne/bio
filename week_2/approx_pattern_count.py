with open('C:/Users/shenme/Desktop/Bio-Informatics/week_2/data/dataset_9_6.txt') as f:
    target = f.readline().strip()

    text = f.readline().strip()

    d = f.readline().strip()

    d = int(d)

    target = "AA"

    text = "TACGCATTACAAAGCACA"

    d = 1

    def hamming_distance(a, b):
        distance = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                distance += 1
        return distance

    start = 0
    count = 0
    while start < len(text) - len(target)+1:
        if hamming_distance(text[start:start+len(target)], target) <= d:
            count += 1
        start += 1
    print(count)
