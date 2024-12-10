import sys
import os
import util

use_exampleData = False

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

trails = tuple([tuple([int(x) for x in row]) for row in rows])

trailheads = [ (x , y) for y, row in enumerate(trails) for x, val in enumerate(row) if val == 0]

print(*trails, sep='\n')
print(trailheads)

# scores[part1, part2]
scores = [0,0]
for trailhead in trailheads:
    trailPaths = []
    scores = list(map(lambda x, y: x + y, scores, util.findPath(trails, trailhead, trailPaths)))

print(f"total sum: {scores[0]}")
print(f"total P2 sum: {scores[1]}")
