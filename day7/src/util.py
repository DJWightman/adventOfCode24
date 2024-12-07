def convertToInts(row):
    row[0] = int(row[0])
    temp = row[1].split(' ')
    temp.remove('')
    row[1] = [int(x) for x in temp]

def encodeOperators(key, count, factor):
    ops = []
    for op in range(count):
        ops.append(key % factor)
        key = int(key/factor)
    return ops

def getDigitsInInt(x):
    digits = 0
    while x != 0:
        digits += 1
        x = int(x / 10)
    return digits

def concat(a, b):
    return a * (10**getDigitsInInt(b)) + b

def calculateSolution(solnValues, key, factor):
    ops = encodeOperators(key, len(solnValues)-1, factor)
    soln = solnValues[0]
    for i, op in enumerate(ops):
        if op == 0:
            soln += solnValues[1+i]
        elif op == 1:
            soln *= solnValues[1+i]
        else:
            #soln = int(str(soln) + str(solnValues[1+i]))
            soln = concat(soln, solnValues[1+i])
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