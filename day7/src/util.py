def convertToInts(row):
    row[0] = int(row[0])
    temp = row[1].split(' ')
    temp.remove('')
    row[1] = [int(x) for x in temp]

def encodeOperators(ops, key, count, factor):
    for op in range(count):
        ops.append(key % factor)
        key = int(key/factor)

def calculateSolution(solnValues, key, factor):
    ops = []
    encodeOperators(ops, key, len(solnValues)-1, factor)
    soln = solnValues[0]
    for bit, op in enumerate(ops):
        if op == 0:
            soln += solnValues[1+bit]
        elif op == 1:
            soln *= solnValues[1+bit]
        else:
            soln = int(str(soln) + str(solnValues[1+bit]))
    return soln

def getCalTotal(line,factor):
    target = line[0]
    values = line[1]
    max = len(values) - 1
    for key in range(factor**max):
        soln = calculateSolution(values, key, factor)
        if soln == target:
            print(f"Found: {target}")
            return target
    return 0