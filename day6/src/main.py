import os
import sys

def findStart(cube):
    for y, row in enumerate(cube):
        for x, pos in enumerate(row):
            if pos != '.' and pos != '#':
                return x, y
    
    print("failed")
    return -1, -1

def rotateRight90(cube, x, y):
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

    while x < len(cube) - 1 and cube[y][x+1] != '#':
        cube[y][x] = 'X'
        cube[y][x+1] = '>'
        x += 1

    if x == len(cube) - 1:
        cube[y][x] = 'X'
        ret = True
    
    return ret, cube, x, y

def findPath(cube, x, y):
    ret = False
    while ret == False:
        ret, cube, x, y = moveStraight(cube, x, y)
        cube, x, y = rotateLeft90(cube, x, y)
    return cube

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

cube = [[x for x in row] for row in rows]

x, y = findStart(cube)

cube, x, y = alignStartRight(cube, x, y)

cube = findPath(cube, x, y)

positions = 0
for row in cube:
    for x in row:
        if x == 'X':
            positions += 1

print(f"number of positions:{positions}")
