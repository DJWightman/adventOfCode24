import os
import sys
import util

use_exampleData = True
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
    print(f"Secret Number {i} of {len(secretNumbers)}")
    for ii in range(2000):
        p1 = num % 10
        num = util.newSecretNumber(num)
        delta = (num % 10) - p1
        deltas.append(delta)
        if len(deltas) == 4:
            seq = tuple(deltas)
            if seq not in sequences:
                sequences[seq] = [0, [ 0 for iii in range(len(secretNumbers))]]
            if sequences[seq][1][i] == 0:
                sequences[seq][1][i] = num % 10
                sequences[seq][0] += num % 10
            keys.append(seq)
            deltas.pop(0)

    newSecretNums.append(num)

for i in range(len(secretNumbers)):
    print(secretNumbers[i], ':', newSecretNums[i])

print("Sum is: ", sum(newSecretNums))

sorted_sequences = sorted(sequences.items(), key=lambda x: x[1][0])


print(sorted_sequences[-1][0], " gives max bananas: ", sorted_sequences[-1][1][0])

if use_exampleData:
    print(sorted_sequences[-1][1][1])




