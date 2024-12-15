import os
import sys
import util


use_exampleData = False
if use_exampleData:
    fileName = "example.txt"
else:
    fileName = "data.txt"

dir = os.path.dirname(os.path.abspath(sys.argv[0]))
filePath = dir + "/../input/" + fileName
inputFile = open(filePath, 'r')

grid = []
directions = ''
sub = (0,0)
for line in inputFile:
    if line[0] == '#':
        if '@' in line:
            sub = (line.index('@'), len(grid))
        grid.append(line.replace('\n',''))
    else:
        directions += line.replace('\n','')

grid2, sub2 = util.generate_part2_grid_and_sub(grid)

for i, d in enumerate(directions):
    sub = util.try_move_sub(grid, d, sub)
    sub2 = util.try_move_sub(grid2, d, sub2)

# print(*grid2, sep='\n')

print(f"part1 gps: {util.generate_gps(grid, 'O')}")
print(f"part2 gps: {util.generate_gps(grid2, '[')}")
