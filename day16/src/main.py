import os
import sys
import heapq as hq
import util


use_exampleData = True
if use_exampleData:
    fileName = "example.txt"
else:
    fileName = "data.txt"

dir = os.path.dirname(os.path.abspath(sys.argv[0]))
filePath = dir + "/../input/" + fileName
inputFile = open(filePath, 'r')

dir = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
move = {dir['N']: (0,-1), dir['E']: (1,0), dir['S']: (0,1), dir['W']:(-1,0)}
grid = []
start = ()
finish = ()
for i, line in enumerate(inputFile):
    grid.append(line.replace('\n',''))
    if 'S' in line:
        start = (line.index('S'), i)
    if 'E' in line:
        finish = (line.index('E'), i)


print(*grid, sep='\n')
print(start, finish)
heading = dir['E']

queue = []
seen = set()
hq.heappush(queue, (0, start, heading))

while queue:
    score, position, heading = hq.heappop(queue)

    if position == finish:
        print(score)
        break

    if (position, heading) in seen:
        continue

    seen.add((position, heading))

    surroundings = util.getSurroundings(grid, position)

    for i, x in enumerate(surroundings):
        if x == '#':
            continue
        
        newScore = util.rotateToDirection(heading, i) + 1 + score
        newPosition = tuple(map(lambda a, b: a + b, position, move[i]))
        hq.heappush(queue, (newScore, newPosition, i))

