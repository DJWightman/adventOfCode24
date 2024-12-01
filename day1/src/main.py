import os
import sys

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
    rows.append(line.replace('\n','').split('   '))

column1 = sorted([int(x[0]) for x in rows])
column2 = sorted([int(x[1]) for x in rows])

deltas = [abs(column1[i] - column2[i]) for i in range(len(column1))]
sim_score = [column2.count(column1[i])*column1[i] for i in range(len(column1))]

if use_exampleData:
    print(column1)
    print(column2)
    print(deltas)
    print(sim_score)
    print(f"The length of the list is: {len(column2)}")

print(f"The sum of the deltas is:  {sum(deltas)}")
print(f"The sum of the similarity scores are: {sum(sim_score)}")
