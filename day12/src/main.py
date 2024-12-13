import os
import sys

seen = set()

def getValue(pos, rows):
    return rows[pos[1]][pos[0]]

def getRegions(rows):

    regions = {}
    key = 0
    regions[key] = []
   
    for y, row in enumerate(rows) : 
        for x, val in enumerate(row) :
            newBlocks = [(x, y)]

            while len(newBlocks) > 0:
                pos = newBlocks.pop(0)

                if pos in seen:
                    continue

                seen.add(pos)

                perimeter = 4
                dirs = [(0,1), (0,-1), (1,0), (-1,0)]
                for d in dirs:
                    new = tuple(map(lambda x, y: x + y, pos, d))
                    if 0 <= new[0] < len(rows) and 0 <= new[1] < len(rows):
                        if getValue(new, rows) == getValue(pos, rows):
                            perimeter -= 1
                            if new not in seen:
                                newBlocks.append(new)
                regions[key].append((pos, perimeter))
            if len(regions[key]) > 0:
                key += 1
                regions[key] = []

    if len(regions[key]) == 0:
        regions.pop(key)

    return regions

def getNewSides(mapSize, sweepLine, prevSweepLine):
    changes = [[],[]]
    for c in range(mapSize):
        if (c in prevSweepLine and c in sweepLine) or (c not in prevSweepLine and c not in sweepLine):
            continue
        elif c in prevSweepLine:
            changes[0] += [c]
        else:
            changes[1] += [c]
    sides = 0
    for d in [0,1]:
        if len(changes[d]) > 0:
            sides += 1
        for i, x in enumerate(changes[d][:-1]):
            if changes[d][i + 1] - changes[d][i] > 1:
                sides += 1

    return sides

def sweepDimension(mapSize, regionPoints, vertical):
    x = 0 if vertical else 1
    y = 1 if vertical else 0
    sides = 0
    prevSweepLine = []
    for r in range(mapSize):
        sweepLine = [p[x] for p in regionPoints if p[y] == r]
        if len(sweepLine) == 0:
            continue
        sides += getNewSides(mapSize, sweepLine, prevSweepLine)
        prevSweepLine = sweepLine
    lastSweepLine = []
    return sides + getNewSides(mapSize, lastSweepLine, prevSweepLine)

def getRegionSides(region, mapSize):
    points = [point for (point, perim) in region]
    return sweepDimension(mapSize, points, True) + sweepDimension(mapSize, points, False)     

def getFencing(region, mapSize):
    area = len(region)
    perimeters = [pos[1] for pos in region]
    perimeter = sum(perimeters)
    sides = getRegionSides(region, mapSize)
    return area, perimeter, sides

use_exampleData = False

if use_exampleData:
    fileName = "example4.txt"
else:
    fileName = "data.txt"

dir = os.path.dirname(os.path.abspath(sys.argv[0]))
filePath = dir + "/../input/" + fileName
inputFile = open(filePath, 'r')

rows = []
for line in inputFile:
    rows.append(line.replace('\n',''))
print(*rows, sep='\n')

regions = getRegions(rows)
print(regions)

totalPrice_p1 = 0
totalPrice_p2 = 0
for key, region in regions.items():
    area, perimeter, sides = getFencing(region, len(rows))
    totalPrice_p1 += area * perimeter
    totalPrice_p2 += area * sides
    print(area, perimeter, sides, totalPrice_p1, totalPrice_p2)

print(f"the total price for part 1 is: {totalPrice_p1}")
print(f"the total price for part 2 is: {totalPrice_p2}")
