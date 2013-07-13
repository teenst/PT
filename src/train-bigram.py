#!usr/bin/env python
import sys
from collections import defaultdict

counts = defaultdict(lambda: 0)
context_count = defaultdict(lambda: 0)


# probability = defaultdict(lambda: 0)
# total_count = 0

# file io
training_file = open(sys.argv[1],"r")

for line in training_file:
    line = line.strip()

    words = line.split(" ")
    words.append("</s>")
    words.insert(0,"<s>")
    
    for i in range(1,len(words)-1):
        counts[words[i-1]+" "+words[i]] += 1
        context_count[words[i-1]] +=1
        counts[words[i]] += 1
        context_count[""] += 1
training_file.close()

# # calculate prob
# for word in counts:
#     probability[word] = float(counts[word])/float(total_count)


model_file = open(sys.argv[2],"w")
for ngram,count in sorted(counts.items()):
    words = ngram.split(" ")
    last_element = words.pop()
    context = "".join(words)
    probability = float(counts[ngram])/context_count[context]
    output = "%s\t%f\n" % (ngram,probability)
    model_file.write(output)
