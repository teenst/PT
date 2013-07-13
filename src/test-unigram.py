#!usr/bin/env python
import sys,math
from collections import defaultdict

LAMBDA_1 = 0.95
LAMBDA_UNK = 1 - LAMBDA_1
V = 1000000
W = 0
H = 0

probabilities = defaultdict(lambda: 0)

# read modelfine
model_file = open(sys.argv[1],"r")

for line in model_file:
    line = line.strip()
    w,P = line.split("\t")
    probabilities[w] = float(P)

#test and print
unk = 0
test_file = open(sys.argv[2])
for line in test_file:
    line = line.strip()
    words = line.split(" ")
    words.append("</s>")
    for w in words:
        W += 1
        P = float(LAMBDA_UNK) / float(V)
        if w in probabilities:
            P += LAMBDA_1 * probabilities[w]
        else:
            unk += 1
        H += -math.log(P,2)

print "count = "+str(W)
print "unk = "+str(unk)

        
print "entropy = %f" % (float(H)/float(W))
print "coverage = %f" % (float((W-unk))/W)
