import sys
import os
import util

use_exampleData = True

if use_exampleData:
    fileName = "example.txt"
else:
    fileName = "data.txt"

dir = os.path.dirname(os.path.abspath(sys.argv[0]))
filePath = dir + "/../input/" + fileName
inputFile = open(filePath, 'r')

rows = []
for line in inputFile:
    rows.append(line.replace('\n',''))

cube = [[x for x in row] for row in rows]
max = len(cube) - 1

obstructions = util.getObstructions(cube)
start = util.findStart(cube)
part1_path = [start]
direction = util.getStartDirection(start, cube)
done = False
pos = start.copy()
while done != True:
    pos, done = util.moveForward(pos, direction, obstructions, max)
    part1_path.append(pos)
    direction = util.rotateRight(direction)

length = util.calculateRouteLength(part1_path, max)
print(length)


lines = [[part1_path[i-1], part1_path[i]] for i in range(1, len(part1_path))]
print(*lines, sep='\n')
