import os
import sys
import util

use_exampleData = False
if use_exampleData:
    fileName = "example.txt"
    TARGET_SAVINGS = 50
else:
    fileName = "data.txt"
    TARGET_SAVINGS = 100

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



# shortestPath = util.navigateGrid(grid, start, finish)
# print(len(shortestPath))

shortestPath2 = util.navGrid(grid, start, finish)
print(len(shortestPath2))

# # shortcuts = util.findPart1ShortCuts(shortestPath)
# # shortcuts.sort()

shortcuts = util.findShortcuts2(grid, shortestPath2, 2, TARGET_SAVINGS)

targets = [ (p, s, f) for (p,s,f) in shortcuts if p >= TARGET_SAVINGS]

print(f"Part 1: There are {len(targets)} cheats that save at least {TARGET_SAVINGS} picoseconds")

shortcuts = util.findShortcuts2(grid, shortestPath2, 20, TARGET_SAVINGS)

targets = [ p for (p,s,f) in shortcuts if p >= TARGET_SAVINGS]

print("done search")

print(f"Part 2: There are {len(targets)} cheats that save at least {TARGET_SAVINGS} picoseconds")

set_targets = sorted(set(targets))

if use_exampleData:
    for t in set_targets:
        print(f"There are {targets.count(t)} cheats with {t} picoseconds")

