import csv
from collections import defaultdict
import matplotlib.pyplot as plt


def skills():
    array = []
    with open('data_science_extract.csv', newline='') as File:
        reader = csv.reader(File)
        for i, row in enumerate(reader):
            if i == 0:
                pass
            else:
                array.append(row[7][1:][:-1].split(","))
    return array


listy = skills()
d = defaultdict(int)
for sublist in listy:
    for word in sublist:
        word = word.lower()
        d[word] += 1


d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
for k in d.copy():
    if d[k] <=2:
        del d[k]

plt.figure(figsize=(20,300))
plt.barh(*zip(*d.items()))
plt.savefig('skills-graph3.png')
plt.show()