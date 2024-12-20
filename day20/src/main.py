import os
import sys
import util

use_exampleData = True
if use_exampleData:
    fileName = "example.txt"
else:
    fileName = "data.txt"

dir = os.path.dirname(os.path.abspath(sys.argv[0]))
filePath = dir + "/../input/" + fileName
inputFile = open(filePath, 'r')


grid = []
S = (0,0)
E = (0,0)
for i, line in enumerate(inputFile):
    grid.append(line.replace('\n',''))
    if 'S' in line:
        start = (line.index('S'),i)
    
    if 'E' in line:
        finish = (line.index('E'),i)


print(grid[start[1]][start[0]])

shortestPath = util.navigateGrid(grid, start, finish)

shortcuts = util.findPart1ShortCuts(shortestPath)
shortcuts.sort()

targets = [ (p, s, f) for (p,s,f) in shortcuts if p >=100 ]

print(f"Part 1: There are {len(targets)} cheats that save at least 100 picoseconds")

# shortcuts = []
# for i, pos in enumerate(shortestPath):
#     shortcuts.append(util.findShortcuts(grid, shortestPath, pos))
#     print(i, len(shortcuts[-1]))

print("done search")