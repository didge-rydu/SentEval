import sys
from collections import Counter

filename = sys.argv[1]

labels = []

with open(filename) as f:
  for line in f:
    _, label, _ = line.split('\t')
    labels.append(label)

output = {}
ctr = Counter(labels)

for i, (label, freq) in enumerate(ctr.most_common(len(ctr))):
  output[i] = freq

print([x[0] for x in ctr.most_common(20)])

print(output)
