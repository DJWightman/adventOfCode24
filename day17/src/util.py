import program

results = set()

def findLenMin(low, high, x):

    mid = (high + low) // 2
    if mid == low:
        return mid

    mid_out = program.setRA_and_run(mid)

    if len(mid_out) < x:
        return findLenMin(mid, high, x)
    
    return findLenMin(low, mid, x)

def findLimits():
    min = 0
    max = 0

    newRA = 1
    prev = newRA
    while 1:
        targetLength = program.programLength()
        output = program.setRA_and_run(newRA)

        if len(output) == program.programLength():
            min = findLenMin(prev, newRA, program.programLength()) + 1
        
        if len(output) == program.programLength() + 1:
            max = findLenMin(prev, newRA, program.programLength() + 1)
            break
        
        prev = newRA
        newRA = newRA * 8

    return (min, max)


def findTarget(limits, target, depth):
    min, max = limits
    mid = (max + min) // 2
    
    if mid == min:
        if program.verify(min, target):
            return [min]
        if program.verify(max, target):
            return[max]
        return []
    
    if depth == 5:
        return []
    
    ret = []
    if program.verify(mid, target):
        return [mid]
    
    ret = findTarget((min, mid), target, depth + 1) + findTarget((mid, max), target, depth + 1)
    return list(set(ret))

def findMinInst(limits, instruction_index):
    min, max = limits
    mid = (max + min) // 2
    if min == mid:
        if program.verify(min, instruction_index):
            return mid
        return max
    
    if program.verify(min, instruction_index):
        return min
    
    if program.verify(mid, instruction_index):
        return findMinInst((min, mid), instruction_index)
    return findMinInst((mid, max), instruction_index)

def findMaxInst(limits, instruction_index):
    min, max = limits
    mid = (max + min) // 2
    if min == mid:
        if program.verify(min, instruction_index):
            return mid
        return max
    
    if program.verify(max, instruction_index):
        return max

    if program.verify(mid, instruction_index):
        return findMaxInst((mid, max), instruction_index)
    return findMaxInst((min, mid), instruction_index)

def checkFinalNumbers(limits):
    min, max = limits
    for i in range(min, max + 1):
        if program.verify(i, 0):
            results.add(i)

def checkMids(limits, instruction_index, mids):
    min, max = limits
    mids.sort()
    for m in mids:
        rmin = findMinInst((min, m), instruction_index)
        rmax = findMaxInst((m, max), instruction_index)
        findInstructionLimits((rmin, rmax), instruction_index - 1)

seen = set()
def findInstructionLimits(limits, instruction_index):
    global seen
    if (limits, instruction_index) in seen:
        return
    seen.add((limits, instruction_index))

    mids = findTarget(limits, instruction_index, 0)
    if len(mids) == 0:
        return

    if instruction_index == 0:
        checkFinalNumbers(limits)
    else:
        checkMids(limits, instruction_index, mids)


def findPart2Solutions():
    (min, max) = findLimits()

    min = 0
    for i in reversed(range(program.programLength())):
        t = 0
        while 1:
            if min > max:
                return
            RegA = (min << 3) + t
            if program.verify2(RegA, i):
                min = RegA
                break
            t += 1
    print(min)


def getResults():
    print("Results")
    print(results)