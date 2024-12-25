import os
import sys

use_exampleData = False
if use_exampleData:
    fileName = "example.txt"
else:
    fileName = "data.txt"

dir = os.path.dirname(os.path.abspath(sys.argv[0]))
filePath = dir + "/../input/" + fileName
inputFile = open(filePath, 'r')

inputs = {}
puzzles = []
answer = 0

lines = []
for line in inputFile:
    lines.append(line.replace('\n',''))


print(*lines, sep='\n')

keys = []
locks = []

i = 0
while i < len(lines):
    line = lines[i]

    match line:
        case '#####':
            key = [0,0,0,0,0]
            i += 1
            for ii in range(5):
                key = list(map(lambda a, b: a + b, key, [ 1 if x == '#' else 0 for x in lines[i]]))
                i += 1
            if lines[i] != '.....':
                print("error here")
                exit()
            keys.append(key)
            i += 1
        case '.....':
            lock = [0,0,0,0,0]
            i += 1
            for ii in range(5):
                lock = list(map(lambda a, b: a+b, lock, [ 1 if x == '#' else 0 for x in lines[i] ]))
                i += 1
            if lines[i] != '#####':
                print("error")
                exit()
            locks.append(lock)
            i += 1
        case '':
            i += 1


print("locks:", locks)
print("keys:", keys)

fitting_pairs = 0

for lock in locks:
    for key in keys:
        fit = list(map(lambda a, b: a + b, lock, key))
        overlap = [1 for x in fit if x > 5]
        if overlap:
            print(f"{lock} doesn't fit with {key}")
        else:
            fitting_pairs += 1

print(f"Number of pair fits is: {fitting_pairs}")