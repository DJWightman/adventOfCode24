import os
import sys
from operator import mul

use_exampleData = False

if use_exampleData:
    GRID_X = 11
    GRID_Y = 7
else:
    GRID_X = 101
    GRID_Y = 103
MID_X = int(GRID_X / 2)
MID_Y = int(GRID_Y / 2)
MOVES = 100


if use_exampleData:
    fileName = "example.txt"
else:
    fileName = "data.txt"

dir = os.path.dirname(os.path.abspath(sys.argv[0]))
filePath = dir + "/../input/" + fileName
inputFile = open(filePath, 'r')

robots = []
quadrants = [0,0,0,0]
fg = [[0 for c in range(GRID_X)] for r in range(GRID_Y)]
for line in inputFile:
    p, v = line.replace('\n','').split(' ')
    p = tuple(map(int, p.replace("p=",'').split(",")))
    v = tuple(map(int, v.replace("v=", '').split(",")))
    f = tuple(map(lambda a, b, c: (a + (MOVES * b))%c, p, v, (GRID_X, GRID_Y)))
    robots.append((p, v, f))
    fg[f[1]][f[0]] += 1
    if f[0] < MID_X:
        if f[1] < MID_Y:
            quadrants[0] += 1
        elif f[1] > MID_Y:
            quadrants[1] += 1
    elif f[0] > MID_X:
        if f[1] < MID_Y:
            quadrants[2] += 1
        elif f[1] > MID_Y:
            quadrants[3] += 1

fg = [[str(p) if p > 0 else '.' for p in r ]for r in fg]
#print(*robots, sep='\n')
#print(*fg, sep='\n')
sf = 1
for q in quadrants:
    sf = sf * q
print(f"Robots in quadrants: {quadrants}, safety factor: {sf}")