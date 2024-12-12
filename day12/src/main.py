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

def getFencing(region):
    area = len(region)
    perimeters = [pos[1] for pos in region]
    perimeter = sum(perimeters)
    return area, perimeter, area * perimeter

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
print(*rows, sep='\n')

regions = getRegions(rows)
print(regions)

totalPrice = 0
for key, region in regions.items():
    area, perimeter, price = getFencing(region)
    print(area, perimeter, price)
    totalPrice += price

print(f"the total price is: {totalPrice}")
