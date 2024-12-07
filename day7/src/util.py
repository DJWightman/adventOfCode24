def convertToInts(row):
    row[0] = int(row[0])
    temp = row[1].split(' ')
    temp.remove('')
    row[1] = [int(x) for x in temp]


def getOperatorSizes(row):
    return len(row[1])



