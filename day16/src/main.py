import os
import sys
import heapq as hq
import util


use_exampleData = False
if use_exampleData:
    fileName = "example1.txt"
else:
    fileName = "data.txt"

dir = os.path.dirname(os.path.abspath(sys.argv[0]))
filePath = dir + "/../input/" + fileName
inputFile = open(filePath, 'r')


grid = []
start = ()
finish = ()
for i, line in enumerate(inputFile):
    grid.append(line.replace('\n',''))
    if 'S' in line:
        start = (line.index('S'), i)
    if 'E' in line:
        finish = (line.index('E'), i)

heading = util.dir['E']
path = [start]
score = 0

queue = []
seen = set()
scores = {}
paths = []
bestPath = []
hq.heappush(queue, (score, start, heading, path))

while queue:
    score, position, heading, path = hq.heappop(queue)

    if (position, heading) in seen:
        if scores[position] == score:
            paths.append(path)
        continue

    seen.add((position, heading))

    if position not in scores:
        scores[position] = score

    if position == finish:
        print(f"Best Path Score: {score}")
        bestPath += path
        break

    surroundings = util.getSurroundings(grid, position)
    for newHeading, x in enumerate(surroundings):
        if x == '#':
            continue

        if newHeading == util.reverse_dir[heading]:
            continue

        newPosition = tuple(map(lambda a, b: a + b, position, util.move[newHeading]))
        if (newPosition) in path:
            continue
        
        newPath = [p for p in path] + [newPosition]
        newScore = util.rotateToDirection(heading, newHeading) + 1 + score        

        hq.heappush(queue,(newScore, newPosition, newHeading, newPath))


bestPath_tiles = set(bestPath + [tile for path in paths if path[-1] in bestPath for tile in path ])

print(f"Tiles in best: {len(bestPath_tiles)}")
