import sys
import os
import util

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

line = rows[0]

decoded = util.decodeLine(line)

part1 = util.defragData(decoded)
print(decoded)

checksum = util.computeChecksum(part1)
print(f"checksum is: {checksum}")

dd = util.doubleDecode(decoded)
part2 = util.defrag2(dd)

checksum2 = util.computeChecksum(part2)
print(f"checksum2 is: {checksum2}")