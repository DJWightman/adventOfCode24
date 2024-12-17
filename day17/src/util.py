import bisect

ip = 0
registers = {'A':0, 'B': 0, 'C':0}

combo_op = {0:0, 1:1, 2:2, 3:3, 4:registers['A'], 5:registers['B'], 6:registers['C'], 7:-1}

factory_defaults = ()
instructions = ()
results = set()

def divr(reg_key, op):
    n = registers['A']
    d = 2 ** combo_op[op]
    registers[reg_key] = int(n / d)

def bxor(val1, val2):
    registers['B'] = val1 ^ val2 

def adv(op):
    divr('A', op)

def bdv(op):
    divr('B', op)

def cdv(op):
    divr('C', op)

def bxl(op):
    bxor(op, registers['B'])

def bst(op):
    registers['B'] = combo_op[op] % 8

def jnz(op, ip):
    return ip if registers['A'] == 0 else op - 2

def bxc(op):
    bxor(registers['B'], registers['C'])

def out(op):
    return [str(combo_op[op] % 8)]

def updateCombo():
    combo_op[4] = registers['A']
    combo_op[5] = registers['B']
    combo_op[6] = registers['C']

def cmd(inst, op, ip):
    updateCombo()
    # print(f"inst: {inst}, op: {op}, RA: {registers['A']}, RB: {registers['B']}, RC: {registers['C']}")

    output = []
    match inst:
        case 0:
            adv(op)
        case 1:
            bxl(op)
        case 2:
            bst(op)
        case 3:
            ip = jnz(op, ip)
        case 4:
            bxc(op)
        case 5:
            output = out(op)
        case 6:
            bdv(op)
        case 7:
            cdv(op)
    
    ip += 2
    return ip, output

def run():
    ip = 0
    output = []
    while 1:
        if ip >= len(instructions) - 1:
            break
        ip, po = cmd(instructions[ip], instructions[ip + 1], ip)
        output += po  
    
    return output

def facotryReset():
    registers['A'] = factory_defaults[0]
    registers['B'] = factory_defaults[1]
    registers['C'] = factory_defaults[2]

def setRA_and_run(newRA):
        facotryReset()
        registers['A'] = newRA
        return run()

def findLenMin(low, high, x):

    mid = (high + low) // 2
    if mid == low:
        return mid

    mid_out = setRA_and_run(mid)

    if len(mid_out) < x:
        return findLenMin(mid, high, x)
    
    return findLenMin(low, mid, x)

def findLimits():
    min = 0
    max = 0

    newRA = 1
    prev = newRA
    while 1:

        facotryReset()
        registers['A'] = newRA
        output = run()
        if len(output) == len(instructions):
            min = findLenMin(prev, newRA, len(instructions)) + 1
        
        if len(output) == len(instructions) + 1:
            max = findLenMin(prev, newRA, len(instructions) + 1)
            break
        
        prev = newRA
        newRA = newRA * 8

    return (min, max)


def verify(RA, index):
    ret = True
    out = setRA_and_run(RA)
    for i in reversed(range(len(instructions))):
        if i < index:
            break
        if int(out[i]) != instructions[i]:
            ret = False
            break
    
    return ret


def findTarget(limits, target, depth):
    min, max = limits
    mid = (max + min) // 2
    
    if mid == min:
        if verify(min, target):
            return [min]
        if verify(max, target):
            return[max]
        return []
    
    if depth == 5:
        return []
    
    ret = []
    if verify(mid, target):
        return [mid]
    
    ret = findTarget((min, mid), target, depth + 1) + findTarget((mid, max), target, depth + 1)
    return list(set(ret))

def findMinInst(limits, instruction_index):
    min, max = limits
    mid = (max + min) // 2
    if min == mid:
        # print("verify", min, instruction_index)
        if verify(min, instruction_index):
            return mid
        return max
    
    if verify(min, instruction_index):
        return min
    
    if verify(mid, instruction_index):
        return findMinInst((min, mid), instruction_index)
    return findMinInst((mid, max), instruction_index)

def findMaxInst(limits, instruction_index):
    min, max = limits
    mid = (max + min) // 2
    if min == mid:
        if verify(min, instruction_index):
            return mid
        return max
    
    if verify(max, instruction_index):
        return max

    if verify(mid, instruction_index):
        return findMaxInst((mid, max), instruction_index)
    return findMaxInst((min, mid), instruction_index)

def checkFinalNumbers(limits):
    min, max = limits
    for i in range(min, max + 1):
        if verify(i, 0):
            results.add(i)

def checkMids(limits, instruction_index, mids):
    min, max = limits
    mids.sort()
    for m in mids:
        print(instruction_index, min, m, max)
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


def getResults():
    print("Results")
    print(results)