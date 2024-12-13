import os
import sys

COST_BUTTON_A = 3
COST_BUTTON_B = 1

PART2_OFFSET = 10000000000000

def findMinimumCost(rules):
    A, B, prize = rules
    wins = []
    for pa in range(1,101):
        for pb in range(1,101):
            pos = tuple(map(lambda a, b, x, y: (x*a) + (y*b), A, B, (pa, pa), (pb,pb)))
            if prize == pos:
                cost = (pa * COST_BUTTON_A) + (pb * COST_BUTTON_B)
                wins.append(cost)
    wins.sort()
    if len(wins) > 1:
        print("More than 1 solution")
    cost = wins[0] if len(wins) > 0 else 0
    return (len(wins), cost)

def findMinimumCosts2(rules):
    A, B, prize = rules
    pb = int(((prize[1]*A[0]) - (prize[0]*A[1])) / ((A[0]*B[1]) - (A[1]*B[0])))
    pa = int((prize[0] - (pb*B[0])) / A[0])
    pos = tuple(map(lambda a, b, x, y: (x*a) + (y*b), A, B, (pa, pa), (pb,pb)))
    win = 0
    cost = 0
    if prize == pos:
        win = 1
        cost = (pa * COST_BUTTON_A) + (pb * COST_BUTTON_B)

    return (win, cost)

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

#print(*rows, sep='\n')

total_P1 = (0,0)
total_P2 = (0,0)
for i in range(0,len(rows), 4):
    A = (int(rows[i][rows[i].index('X+')+2:rows[i].index(', Y+')]), int(rows[i][rows[i].index('Y+')+2:]))
    B = (int(rows[i+1][rows[i+1].index('X+')+2:rows[i+1].index(', Y+')]), int(rows[i+1][rows[i+1].index('Y+')+2:]))
    prize = (int(rows[i+2][rows[i+2].index('X=')+2:rows[i+2].index(', Y=')]), int(rows[i+2][rows[i+2].index('Y=')+2:]))
    rules = (A, B, prize)
    #print(rules)
    total_P1 = tuple(map(lambda a, b: a + b, total_P1, findMinimumCosts2(rules)))
    prize2 = tuple(map(lambda x: x + PART2_OFFSET, prize))
    rules2 = (A, B, prize2)
    total_P2 = tuple(map(lambda a, b: a + b, total_P2, findMinimumCosts2(rules2)))


print(f"Part 1: Total wins: {total_P1[0]}, Total cost for wins: {total_P1[1]}")
print(f"Part 2: Total wins: {total_P2[0]}, Total cost for wins: {total_P2[1]}")



