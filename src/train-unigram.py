#!usr/bin/env python
import sys
from collections import defaultdict

counts = defaultdict(lambda: 0)
probability = defaultdict(lambda: 0)
total_count = 0

# file io
training_file = open(sys.argv[1],"r")

for line in training_file:
    line = line.strip()

    words = line.split(" ")
    words.append("</s>")
    for word in words:
        counts[word] += 1
        total_count  += 1
training_file.close()

# calculate prob
for word in counts:
    probability[word] = float(counts[word])/float(total_count)


model_file = open(sys.argv[2],"w")
for word, num in sorted(probability.items()):
    output = "%s\t%f\n" % (word,num)
    model_file.write(output)
    
