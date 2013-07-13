#!usr/bin/env python
import sys,math
from collections import defaultdict

LAMBDA_1 = 0.95
LAMBDA_2 = 0.95
LAMBDA_UNK = 1 - LAMBDA_1
V = 1000000
W = 0
H = 0

probabilities =defaultdict(lambda: 0)
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
    words.insert(0,"<s>")
    for i in range(1,len(words)-1):
        P1 = float(LAMBDA_1) * probabilities[words[i]] + float(LAMBDA_UNK) / float(V)
        P2 = float(LAMBDA_2) * probabilities[words[i-1]+" "+words[i]] + float(1-LAMBDA_2) * float(P1)
        H += -math.log(P2,2)
        W += 1
print "entropy = %f" % (float(H)/float(W))

