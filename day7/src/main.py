import sys
import os
import util
import time

start_time = time.time()
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
    rows.append(line.replace('\n','').split(':'))

calTotal = 0
part2 = 0

for i, row in enumerate(rows):
    util.convertToInts(row)
    calTotal += util.getCalTotal(row,2)
    part2 += util.getCalTotal(row,3)

print(f"calibration Total: {calTotal}")
print(f"Part2 calibration Total: {part2}")
print(f"total time to execute: {time.time() - start_time}")

