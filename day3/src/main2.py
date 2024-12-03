import os
import sys

def cleanLine(row, newRow, on, index, length):
    if on == True:
        newRow += row[:index]
    row = row[index + length:]

    return newRow, row
       
def parseInstructions(on, row):
    newRow = ''
    while row.find('do()') >=0 or row.find('don\'t()') >=0:
        firstOn = row.find('do()')
        firstOff = row.find('don\'t()')

        if firstOn < 0:
            firstOn = firstOff + 1
        if firstOff < 0:
            firstOff = firstOn + 1

        if firstOff < firstOn:
            index = firstOff
            length = len('don\'t()')
            newOn = False
        else:
            index = firstOn
            length = len('do()')
            newOn = True
        newRow, row = cleanLine(row, newRow, on, index, length)
        on = newOn
    
    if on == True:
        newRow += row

    return on, newRow

def processRow(row):
    rowList = row.split(')')
    while rowList.count(''):
        rowList.remove('')

    rowList = [ x.split('mul(') for x in rowList]

    rowList = [ x[-1] for x in rowList]

    rowList = [x.split(',') for x in rowList]

    sum = 0
    for x in rowList:
        tempMul = 0
        if len(x) != 2:
            continue
        if x[0].isnumeric() == False or x[1].isnumeric() == False:
            continue
        sum += int(x[0])*int(x[1])
    
    return sum

def main():
    use_exampleData = False

    if use_exampleData:
        fileName = "example2.txt"
    else:
        fileName = "data.txt"

    dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    filePath = dir + "/../input/" + fileName
    inputFile = open(filePath, 'r')

    rows = []
    for line in inputFile:
        rows.append(line.replace('\n',''))

    sum = 0
    sum_part2 = 0
    on = True
    for row in rows:
        sum += processRow(row)
        on, newRow = parseInstructions(on, row)
        sum_part2 += processRow(newRow)
    print(f"sum is: {sum}, part2 sum is {sum_part2}")


if __name__ == "__main__":
    main()