import os
import sys
import util
import heapq as hq

use_exampleData = False
if use_exampleData:
    fileName = "example.txt"
    GRID_SIZE = 7
    DATA_SIZE = 12
else:
    fileName = "data.txt"
    GRID_SIZE = 71
    DATA_SIZE = 1024
dir = os.path.dirname(os.path.abspath(sys.argv[0]))
filePath = dir + "/../input/" + fileName
inputFile = open(filePath, 'r')


data = []
for line in inputFile:
    data.append(tuple(map(int,line.replace('\n','').split(','))))

fd = data[:DATA_SIZE]
moves = util.navigateGrid(fd, GRID_SIZE)
print("Part 1 number of steps: ", moves)

position = util.findFirstPosition(DATA_SIZE, len(data), data, GRID_SIZE)

