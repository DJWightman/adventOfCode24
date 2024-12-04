import os
import sys

def transpose(cube):
    length = len(cube)
    tCube = []
    for i in range(length):
        line = []
        for ii in range(length):
            line.append(rows[ii][i])
        tCube.append(line)
    return tCube

def rotate(cube):
    length = len(cube)
    rCube = []
    for i in range(length):
        line = []
        for ii in reversed(range(length)):
            line.append(cube[ii][i])
        rCube.append(line)
    return rCube

def createDiagonal(cube):
    length = len(cube)
    diagonal = []
    for i in range(length):
        line = []
        for ii in range(i+1):
            line.append(cube[i-ii][ii])
        diagonal.append(line)

    for i in range(1,length):
        line = []
        for ii in range(length - i):
            line.append(cube[length - 1 - ii][i + ii])
        diagonal.append(line)

    return diagonal


def makeListofStrings(cube):
    los = []
    for row in cube:
        sLine = ""
        for c in row:
            sLine += c
        los.append(sLine)
    return los

def getXMASCount(cube):
    count = 0
    los = makeListofStrings(cube)
    for row in los:
        count += row.count("XMAS")
        count += row.count("SAMX")
    return count

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

cube1 = [[x for x in row] for row in rows]

cube2 = transpose(cube1)

cube3 = createDiagonal(cube1)

cube4 = createDiagonal(rotate(cube1))

totalCount = 0
totalCount += getXMASCount(cube1)
totalCount += getXMASCount(cube2)
totalCount += getXMASCount(cube3)
totalCount += getXMASCount(cube4)

print(f"The total count is:{totalCount}")

