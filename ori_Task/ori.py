with open('C:/Users/shenme/Desktop/Bio-Informatics/ori_Task/dataset_2_6.txt') as f:
    text = f.readline()
    print(text)
    target = f.readline().strip()
    print(target)
    count = 0
    start = 0
    while start < len(text):
        pos = text.find(target, start)
        if pos != -1:
            start = pos + 1
            count += 1
        else:
            break

    print('first string:' + str(count))
