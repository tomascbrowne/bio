with open('C:/Users/shenme/Desktop/Bio-Informatics/ori_Task/dataset_2_13.txt') as f:
    # text = f.readline()
    text = "CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA"
    print(text)
    # k_mer = f.readline().strip()
    # k_mer = int(k_mer)
    k_mer = 3
    print(k_mer)
    count = 0
    freq_kmer = dict()
    max_count = 0
    while count < len(text) - k_mer + 1:
        pattern = text[count:count + k_mer]
        if pattern in freq_kmer:
            freq_kmer[pattern] += 1
            if (freq_kmer[pattern] > max_count):
                max_count = freq_kmer[pattern]
        else:
            freq_kmer.pop
            freq_kmer[pattern] = 1

        count += 1

    print(freq_kmer)

    for k in freq_kmer:
        if freq_kmer.get(k) == max_count:
            print(k, end=" ")
