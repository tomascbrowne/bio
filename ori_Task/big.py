# def freqKmers(text, k_mer, i):
#     k_mer = int(k_mer)
#     count = 0
#     max_count = 0
#     while count < len(text) - (k_mer+1):
#         pattern = text[count:count + k_mer]
#         if pattern in freq_kmer:
#             if i+count not in freq_kmer_pos:
#                 freq_kmer_pos[i+count] = pattern
#                 freq_kmer[pattern] += 1
#         else:
#             freq_kmer_pos[i+count] = pattern
#             freq_kmer[pattern] = 1
#         count += 1


with open('C:/Users/shenme/Desktop/Bio-Informatics/ori_Task/dataset_4_5.txt') as f:
    text = f.readline().strip()
    # print(text)
    k = f.readline().strip()
    k = int(k)
    print(k)
    L = f.readline().strip()
    L = int(L)
    print(L)
    t = f.readline().strip()
    t = int(t)
    print(t)

    i = 0

    freq_kmer = dict()
    freq_kmer_pos = dict()
    count = 0

    while i < len(text) - (k+1):
        pattern = text[i:i + k]
        if pattern in freq_kmer_pos:
            freq_kmer_pos[pattern].append(i)
            # freq_kmer[pattern] += 1
        else:
            # freq_kmer[pattern] = 1
            freq_kmer_pos[pattern] = [i]
            # there should be a way to count the clumps within this while loop
        # if len(freq_kmer_pos[pattern]) == t and (freq_kmer_pos[pattern][t-1]+k - freq_kmer_pos[pattern][0] < L):
        #     count += 1
        i += 1

    # print(freq_kmer)
    # print(freq_kmer_pos)
    for key in freq_kmer_pos:
        current_Pattern_Positions = freq_kmer_pos[key]
        for j in range(len(current_Pattern_Positions) - t + 1):
            total = (
                current_Pattern_Positions[j+2]+k) - (current_Pattern_Positions[j])
            if total <= L:
                count += 1
                break

print(count)
