import os
import sys

def processRow(row):
    temp = row
    print(temp)
    temp2 = temp.split(')')
    while temp2.count(''):
        temp2.remove('')
    print(temp2)
    temp3 = [ x.split('mul(') for x in temp2]
    print(temp3)
    temp4 = [ x[-1] for x in temp3]
    print(temp4)
    temp5 = [x.split(',') for x in temp4]
    print(temp5)
    sum = 0
    for x in temp5:
        tempMul = 0
        if len(x) != 2:
            continue
        if x[0].isnumeric() == False or x[1].isnumeric() == False:
            continue
        # print(f"happy x:{int(x[0])} , y: {x[1]}")
        sum += int(x[0])*int(x[1])
    
    return sum

def main():
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

    #print(rows)
    sum = 0
    for row in rows:
        sum += processRow(row)
    print(f"sum is: {sum}")

if __name__ == "__main__":
    main()