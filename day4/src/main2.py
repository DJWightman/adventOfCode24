import os
import sys

def checkM(char):
    if char == 'M':
        return 1
    return 0

def checkS(char):
    if char == 'S':
        return 1
    return 0

def isMAS(cube, x, y):
    MAS = 0
    if checkM(cube[x-1][y-1]) and checkS(cube[x+1][y+1]):
        MAS += 1
    elif checkS(cube[x-1][y-1]) and checkM(cube[x+1][y+1]):
        MAS += 1

    if checkM(cube[x-1][y+1]) and checkS(cube[x+1][y-1]):
        MAS += 1
    elif checkS(cube[x-1][y+1]) and checkM(cube[x+1][y-1]):
        MAS += 1
    
    if MAS == 2:
        print(f"found at: {x},{y}")
        return 1
    return 0

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

length = len(rows)

cube = [[x for x in row] for row in rows]

count = 0
for i in range(1,length - 1):
    for ii in range(1,length - 1):
        if cube[i][ii] == 'A':
            count += isMAS(cube, i, ii)

print(f"The X-MAS count is:{count}")
