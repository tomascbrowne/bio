import matplotlib.pyplot as plt
import math

mf = open('C:/Users/shenme/Desktop/Bio-Informatics/week_2/data/Salmonella.txt', "r+")
file_text = mf.readline().strip()

text = ""

while file_text:
    text += file_text
    file_text = mf.readline().strip()

print(len(text))
buckets = [0] * math.ceil(len(text) / 100000)
print(len(buckets))
index = 0
for e in text:
    if e == "C":
        buckets[math.floor(index/100000)] += 1
    index += 1

x = [0] * math.ceil(len(text) / 100000)
for e in range(len(x)):
    x[e] = e

plt.plot(x, buckets)

plt.ylabel('Cytosine count')
plt.xlabel('block (in 10,000 increments)')

plt.title('Cytosine count in 100,000 block increments')

plt.show()

genome = list(text)
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
        with open('C:/Users/shenme/Desktop/Bio-Informatics/week_2/data/salm_ori', 'w') as f:
            f.write(text[i+1-425:i+1+425])
