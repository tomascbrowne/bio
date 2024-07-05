with open("C:/Users/shenme/Desktop/Bio-Informatics/week_2/data/dataset_9_3.txt") as f:
    # text = f.readline().strip()
    # print(text)
    # target = f.readline().strip()
    # print(target)

    text = "CAGAAAGGAAGGTCCCCATACACCGACGCACCAGTTTA"

    target = "CACGCCGTATGCATAAACGAGCCGCACGAACCAGAGAG"

    distance = 0
    for i in range(len(text)):
        if text[i] != target[i]:
            distance += 1
    print(distance)

    def hamming_distance(m_1, m_2):
        return sum(s1 != s2 for s1, s2 in zip(m_1, m_2))
