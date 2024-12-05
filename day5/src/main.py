import os
import sys


def getRules(rows):
    rules = []
    for i, row in enumerate(rows):
        if row == '':
            return rows[i+1:], rules
        rules.append(row.split('|'))

def getUpdates(rows):
    updates = []
    for row in rows:
        updates.append(row.split(','))
    return updates

def checkUpdate(update, rules):
    for i, page in enumerate(update):
        relevantRules = [rule for rule in rules if rule[0] == page]
        prePage = update[:i]
        for rule in relevantRules:
            if prePage.count(rule[1]):
                return False
    return True

def reorderUpdate(update, rules):
    for i, page in enumerate(update):
        if i == 0:
            continue
        relevantRules = [rule for rule in rules if rule[0] == page]
        prePage = update[:i]
        for rule in relevantRules:
            if prePage.count(rule[1]):
                index = update.index(rule[1])
                poppedPage = update.pop(index)
                update.insert(i,poppedPage)
                return False
    return True

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

rows, rules = getRules(rows)
updates = getUpdates(rows)

rules = sorted(rules, key=lambda x: (x[0], x[1]))

middlePages_p1 = []
middlePages_p2 = []
for update in updates:
    if checkUpdate(update, rules):
        middleIndex = int(len(update)/2)
        middlePages_p1.append(int(update[middleIndex]))
    else:
        while 1:
            if reorderUpdate(update, rules):
                break
        
        middleIndex = int(len(update)/2)
        middlePages_p2.append(int(update[middleIndex]))

print(middlePages_p1)
print(f"The sum of correct middles is:{sum(middlePages_p1)}")
print(middlePages_p2)
print(f"The sum of reordered middles is:{sum(middlePages_p2)}")
