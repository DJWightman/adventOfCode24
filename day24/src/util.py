def performAction(i1, i2, action):
    match action:
        case "AND":
            return i1 & i2
        case "OR":
            return i1 | i2
        case "XOR":
            return i1 ^ i2


def solvePuzzle(puzzles, inputs, out, depth):

    if depth >= 100:
        return False, -1

    k1 = puzzles[out][0]
    k2 = puzzles[out][1]
    action = puzzles[out][2]

    if k1[0] in 'xy':
        return True, performAction(inputs[k1], inputs[k2], action)
    
    ret1, bit1 = solvePuzzle(puzzles, inputs, k1, depth +1)
    ret2, bit2 = solvePuzzle(puzzles, inputs, k2, depth + 1)

    if ret1 and ret2:
        return ret1, performAction(bit1, bit2, action)
    return False, -1

def clearInputs(inputs):
    for k, v in inputs.items():
        inputs[k] = 0

def getFinalOutput(puzzles, inputs, z_length):
    output = 0
    for i in range(z_length + 1):
        out = 'z' + f"{i:02}"
        ret, bit = solvePuzzle(puzzles, inputs, out, 0)
        if ret:
            output |= bit << i
        else:
            return -1
    
    return output


def testPuzzles(puzzles, inputs, i, z_length):

    kx = 'x' + f"{i:02}"
    ky = 'y' + f"{i:02}"

    clearInputs(inputs)

    inputs[kx] = 1
    x = 1 << i
    y = 0

    z = getFinalOutput(puzzles, inputs, z_length)

    if z != y + x:
        return False
    
    clearInputs(inputs)

    inputs[ky] = 1
    y = 1 << i
    x = 0

    z = getFinalOutput(puzzles, inputs, z_length)

    if z != y + x:
        return False
    
    clearInputs(inputs)

    inputs[kx] = 1
    inputs[ky] = 1
    x = 1 << i
    y = 1 << i

    z = getFinalOutput(puzzles, inputs, z_length)

    if z != y + x:
        return False
    
    return True



def getGates(puzzles, out, roots):

    k1 = puzzles[out][0]
    k2 = puzzles[out][1]

    if k1[0] in 'xy':
        return roots
    
    return getGates(puzzles, k1, roots + [k1]) + getGates(puzzles, k2, roots + [k2])

def rootsOkay(puzzles, out, target):

    k1 = puzzles[out][0]
    k2 = puzzles[out][1]

    if k1[0] in 'xy':
        if int(k1[1:]) <= target:
            return True
        return False
    
    return rootsOkay(puzzles, k1, target) and rootsOkay(puzzles, k2, target)

