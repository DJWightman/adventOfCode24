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

l_chars = []
for row in rows:
    for pos in row:
        if pos != '.' and l_chars.count(pos) == 0:
            l_chars.append(pos)

chars = { pos for row in rows for pos in row if pos != '.'}

grid = [[x for x in row] for row in rows ]
#print(*grid,sep='\n')
print(chars)

print(f"Grid height: {len(grid)}, grid width: {len(grid[0])}")
gridLength = len(grid)

antinodes = []
part2 = []
for char in chars:
    locations = util.findCharLocations(grid, char)
    for i, location in enumerate(locations[:-1]):
        util.getAntinodes(location, locations[i+1:],gridLength - 1, antinodes, True)
        util.getAntinodes(location, locations[i+1:],gridLength - 1, part2, False)

print(f"Count of antinodes: {len(antinodes)}")
print(f"Part2 Count of antinodes: {len(part2)}")