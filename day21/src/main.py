import os
import sys
import util

use_exampleData = False
if use_exampleData:
    fileName = "example.txt"
    NUM_ROBOTS = 2
else:
    fileName = "data.txt"
    NUM_ROBOTS = 25

dir = os.path.dirname(os.path.abspath(sys.argv[0]))
filePath = dir + "/../input/" + fileName
inputFile = open(filePath, 'r')

codes = []

for line in inputFile:
    codes.append(line.replace('\n',''))

print(*codes, sep='\n')


p1_complexity = []
p2_complexity = []
for code in codes:
    p1_len = 0
    p2_len = 0
    pos = (2,3)
    for c in code:
        l1, ks = util.shortestPath(c, pos, 2)
        l2, ks2 = util.shortestPath(c, pos, 25)
        p1_len += l1
        p2_len += l2
        pos = util.getMoveCoords(c, util.keypad)


    p2_complexity += [(p2_len, util.getCodeNum(code))]
    p1_complexity += [(p1_len , util.getCodeNum(code))]


print(p1_complexity)
print(p2_complexity)

p1_complexity = [ a * b for a,b in p1_complexity]
print(p1_complexity)

p2_complexity = [ a * b for a,b in p2_complexity]
print(p2_complexity)

print(f"Total part 1 p1_complexity: {sum(p1_complexity)}")

print(f"Total part 2 p1_complexity: {sum(p2_complexity)}")