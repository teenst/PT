#!usr/bin/env python
import sys
from collections import defaultdict

word_frequency = defaultdict(lambda: 0)

# file ip
input_file =  open(sys.argv[1], "r")

#  
for line in input_file:
    line = line.strip()

    words = line.split(" ")

    for word in words:
        word_frequency[word] += 1

for key,value in sorted(word_frequency.items()):
    print "%s\t%r" % (key,value)
    
