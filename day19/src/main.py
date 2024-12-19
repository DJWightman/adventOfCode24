import os
import sys
import util

use_exampleData = False
if use_exampleData:
    fileName = "example.txt"
else:
    fileName = "data.txt"

dir = os.path.dirname(os.path.abspath(sys.argv[0]))
filePath = dir + "/../input/" + fileName
inputFile = open(filePath, 'r')


availableDesigns = ()
desiredPatterns = []
for i, line in enumerate(inputFile):
    if i == 0:
        availableDesigns = tuple(line.replace('\n','').split(', '))
        continue
    
    line = line.replace('\n','')
    if len(line) == 0:
        continue

    desiredPatterns.append(line)


print(availableDesigns)
print(*desiredPatterns,sep='\n')

possibleDesigns = 0
part2Combinations = 0

for desired in desiredPatterns:
    # print("desired Pattern:", desired)
    ret = util.desiredPatternPossible(availableDesigns, desired)
    if ret > 0:
        possibleDesigns += 1
    part2Combinations += ret

print("Part 1 - possible designs:", possibleDesigns)
print("Part 2 - possible designs:", part2Combinations)