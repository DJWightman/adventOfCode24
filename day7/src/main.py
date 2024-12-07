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
    rows.append(line.replace('\n','').split(':'))

calTotal = 0

for i, row in enumerate(rows):
    util.convertToInts(row)
    nums = row[1]
    max = len(nums) - 1
    for ii in range(2**max):
        s = f"Row {i} Max {max} Soln {ii}:"
        soln = nums[0]
        for bit in range(max):
            x = (ii >> bit) & 1
            if x == 0:
                s += "add,"
                soln += nums[1+bit]
            else:
                s +="multiply,"
                soln *= nums[1+bit]
        #print(s)
        if soln == row[0]:
            print("Soln found")
            calTotal += row[0]
            break

print(f"calibration Total:{calTotal}")



