#the first agument must be the file to calculate against
#example: python entropy.py README.md

import math
import sys
from sets import Set
with open(sys.argv[1], 'r') as myfile:
    data=myfile.read().replace('\n', '')
st = data
stList = list(st)
alphabet = list(Set(stList))
freqList = []
for symbol in alphabet:
    ctr = 0
    for sym in stList:
        if sym == symbol:
            ctr += 1
    freqList.append(float(ctr) / len(stList))
ent = 0.0
for freq in freqList:
    ent = ent + freq * math.log(freq, 2)
ent = -ent
print ent
