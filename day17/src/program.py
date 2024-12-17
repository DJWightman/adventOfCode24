ip = 0
registers = {'A':0, 'B': 0, 'C':0}

combo_op = {0:0, 1:1, 2:2, 3:3, 4:registers['A'], 5:registers['B'], 6:registers['C'], 7:-1}

factory_defaults = ()
instructions = ()

def setRegisters(A,B,C):
    registers['A'] = A
    registers['B'] = B
    registers['C'] = C
    global factory_defaults
    factory_defaults = (A,B,C)

def setInstructions(insts):
    global instructions
    instructions = insts

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

def setRA_and_run(RegA):
        facotryReset()
        registers['A'] = RegA
        return run()

def programLength():
    return len(instructions)

def verify(RA, index):
    ret = True
    out = setRA_and_run(RA)
    for i in reversed(range(programLength())):
        if i < index:
            break
        if int(out[i]) != instructions[i]:
            ret = False
            break
    
    return ret