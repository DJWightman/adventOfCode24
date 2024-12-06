import os
import sys

gps = 0

def findStart(cube):
    for y, row in enumerate(cube):
        for x, pos in enumerate(row):
            if pos != '.' and pos != '#':
                return x, y
    
    print("failed")
    return -1, -1

def rotateRight90(cube, x, y):
    global gps
    gps = gps + 1 if gps < 3 else 0
    length = len(cube)
    newCube = []
    for i in range(length):
        line = []
        for ii in range(length):
            line.append(cube[length - 1 - ii][i])
        newCube.append(line)
    new_x = length - 1 - y
    new_y = x
    return newCube, new_x, new_y

def rotateLeft90(cube, x, y):
    global gps
    gps = gps - 1 if gps > 0 else 3
    length = len(cube)
    newCube = []
    for i in range(length):
        line = []
        for ii in range(length):
            line.append(cube[ii][length - 1 - i])
        newCube.append(line)
    new_x = y
    new_y = length - 1 - x
    return newCube, new_x, new_y

def alignStartRight(cube, x, y):
    if cube[y][x] == '^':
        cube, x, y = rotateRight90(cube, x, y)
    elif cube[y][x] == '<':
        cube, x, y = rotateRight90(cube, x, y)
        cube, x, y = rotateRight90(cube, x, y)

    elif cube[y][x] == 'v':
        cube, x, y = rotateRight90(cube, x, y)
        cube, x, y = rotateRight90(cube, x, y)
        cube, x, y = rotateRight90(cube, x, y)
    
    cube[y][x] = '>'
    return cube, x, y

def moveStraight(cube,x,y):
    ret = False

    while x < len(cube) - 1 and (cube[y][x+1] != '#' and cube[y][x+1] != 'O'):
        cube[y][x] = 'X'
        cube[y][x+1] = '>'
        x += 1

    if x == len(cube) - 1:
        cube[y][x] = 'X'
        ret = True
    
    return ret, cube, x, y

def getCornerCoord(x,y, length):
    global gps
    local_gps = gps
    while local_gps != 0:
        local_gps = local_gps - 1 if local_gps > 0 else 3
        new_x = y
        y = length - 1 - x
        x = new_x
    return [x, y]


def findPath(cube, x, y):
    corners = []
    ret = False
    delta_count = 0
    while ret == False:
        ret, cube, newx, y = moveStraight(cube, x, y)
        delta = newx-x
        x = newx
        cube, x, y = rotateLeft90(cube, x, y)
        if delta == 0:
            delta_count += 1
            if delta_count >= 4:
                return True
            continue
        else:
            delta_count = 0
        cornerCoord = getCornerCoord(x,y,len(cube))
        if corners.count(cornerCoord) == 1:
            return True, cube
        corners.append(cornerCoord)
    return False, cube

def findPositions(cube):
    positions = []
    for y, row in enumerate(cube):
        for x, pos in enumerate(row):
            if pos == 'X':
                positions.append([x,y])
    print(f"number of positions:{len(positions)}")
    return positions

def addObstruction(cube, position):
    x = position[0]
    y = position[1]   
    cube[y][x] = 'O'

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

cube_start = [[x for x in row] for row in rows]

x_start, y_start = findStart(cube_start)
start_position = [x_start,y_start]

cube, x, y = alignStartRight(cube_start, x_start, y_start)
infLoop, part1_cube = findPath(cube, x, y)

while gps != 0:
    part1_cube, temp, temp = rotateLeft90(part1_cube, 0, 0)

possiblePositions = findPositions(part1_cube)
possiblePositions.remove(start_position)

loopCount = 0
for i, obstruction in enumerate(possiblePositions):
    print(i)
    newCube = [row[:] for row in cube_start]
    addObstruction(newCube, obstruction)

    newCube, x, y = alignStartRight(newCube, x_start, y_start)
    infLoop, part1_cube = findPath(newCube, x, y)

    if infLoop:
        loopCount += 1

print(f"The number of possible loops is: {loopCount}")
