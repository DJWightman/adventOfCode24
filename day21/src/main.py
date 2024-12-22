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


complexity = []
derp = []
for code in codes:
    sequence = ''
    pos = (2,3)
    herp = 0
    for c in code:
        s, ks = util.shortestPath(c, pos, 2)
        
        l, ks2 = util.shortestPath2(c, pos, 2)
        # print(l)
        sequence += s
        herp += l
        # print(ks, ":", ks2)
        # print(len(s),':', l)

        pos = util.getMoveCoords(c, util.keypad)

    # print(sequence)
    # print(len(sequence))
    # print(util.getCodeNum(code))
    derp += [(herp, util.getCodeNum(code))]
    complexity += [ (len(sequence) , util.getCodeNum(code))]


print(complexity)
print(derp)

complexity = [ a * b for a,b in complexity]
print(complexity)

derp = [ a * b for a,b in derp]
print(derp)

print(f"Total part 1 complexity: {sum(complexity)}")

print(f"Total part 2 complexity: {sum(derp)}")