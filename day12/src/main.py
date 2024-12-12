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

def getDeltas(length, xs, lastRow):
    deltas = [[],[]]
    for c in range(length):
        if (c in lastRow and c in xs) or (c not in lastRow and c not in xs):
            continue
        elif c in lastRow:
            deltas[0] += [c]
        else:
            deltas[1] += [c]
    return deltas

def checkDeltas(deltas):
    sides = 0
    for d in [0,1]:
        if len(deltas[d]) > 0:
            sides += 1
        for i, x in enumerate(deltas[d][:-1]):
            if deltas[d][i + 1] - deltas[d][i] > 1:
                sides += 1
    return sides

def loopDimension(length, ps, dim):
    sides = 0
    lastRow = []
    for r in range(length):
        xs = [p[dim[0]] for p in ps if p[dim[1]] == r]
        if len(xs) == 0:
            continue
        deltas = getDeltas(length, xs, lastRow)
        sides += checkDeltas(deltas)
        lastRow = xs
    
    xs = []
    deltas = getDeltas(length, xs, lastRow)
    sides += checkDeltas(deltas)

    return sides

def getSides(region, length):
    ps = [pos for (pos, perim) in region]
    return loopDimension(length, ps, (0,1)) + loopDimension(length, ps, (1,0))     

def getFencing(region, length):
    area = len(region)
    perimeters = [pos[1] for pos in region]
    perimeter = sum(perimeters)
    # corners = findCorners(region)
    sides = getSides(region, length)
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
