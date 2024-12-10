import sys
import os

directions = [(1,0), (-1,0), (0,1), (0,-1)]

def findPath(pos, trails, peaks, part2):
    max = len(trails)
    currentVal = trails[pos[1]][pos[0]]
    if currentVal == 9:
        if part2:
            return 1
        elif pos not in peaks:
            peaks.append(tuple(pos))
            return 1
        else:
            return 0

    ret = 0
    for d in directions:
        x = pos[0] + d[0]
        y = pos[1] + d[1]
        if  (
                x < max and
                x >= 0 and
                y < max and
                y >= 0
            ) and trails[y][x] - currentVal == 1:
            ret += findPath((x, y), trails, peaks, part2)
    
    return ret


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

trails = [[int(x) for x in row] for row in rows]

trailheads = [ (x , y) for y, row in enumerate(trails) for x, val in enumerate(row) if val == 0]

print(*trails, sep='\n')
print(trailheads)

scores = []
scores_p2 = []
for trailhead in trailheads:
    trailPaths = []
    scores.append(findPath(trailhead, trails, trailPaths, 0))
    scores_p2.append(findPath(trailhead, trails, trailPaths, 1))

print(f"total sum: {sum(scores)}")

print(f"total P2 sum: {sum(scores_p2)}")