import os
import sys
import util

use_exampleData = False
if use_exampleData:
    fileName = "example1.txt"
    NUM_ROBOTS = 2
else:
    fileName = "data.txt"
    NUM_ROBOTS = 25

dir = os.path.dirname(os.path.abspath(sys.argv[0]))
filePath = dir + "/../input/" + fileName
inputFile = open(filePath, 'r')

secretNumbers = []

for line in inputFile:
    secretNumbers.append(int(line.replace('\n','')))

sequences = {}
keys = []
deltas = []
newSecretNums = []
for i, sn in enumerate(secretNumbers):
    num = sn
    for ii in range(2000):
        p1 = num % 10
        num = util.newSecretNumber(num)
        delta = (num % 10) - p1
        deltas.append(delta)
        if len(deltas) == 4:
            seq = tuple(deltas)
            if seq not in sequences:
                sequences[seq] = [ 0 for iii in range(len(secretNumbers))]
            if sequences[seq][i] == 0:
                sequences[seq][i] = num % 10
            keys.append(seq)
            deltas.pop(0)

    newSecretNums.append(num)

for i in range(len(secretNumbers)):
    print(secretNumbers[i], ':', newSecretNums[i])

print("Sum is: ", sum(newSecretNums))


maxBananas = 0
bananas = []
for i, key in enumerate(keys):
    print(f"{i} of {len(keys)}: {int(i/len(keys)*100)}%")
    bananas.append((sum(sequences[key]), key))

bananas.sort()

print(bananas[-1][1], " gives max bananas: ", bananas[-1][0])

if use_exampleData:
    print(sequences[bananas[-1][1]])




