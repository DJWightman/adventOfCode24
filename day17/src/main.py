import os
import sys
import util

use_exampleData = False
if use_exampleData:
    fileName = "example1.txt"
else:
    fileName = "data.txt"

dir = os.path.dirname(os.path.abspath(sys.argv[0]))
filePath = dir + "/../input/" + fileName
inputFile = open(filePath, 'r')


instructions = ()
for line in inputFile:
    line.replace('\n', '')
    try:
        g, a = line.split(':')
    except:
        continue
    match g:
        case "Register A":
            util.registers['A'] = int(a)
        case "Register B":
            util.registers['B'] = int(a)
        case "Register C":
            util.registers['C'] = int(a)
        case "Program":
            instructions = tuple([int(x) for x in a.split(',')])
        case _:
            continue

print(f"A:{util.registers['A']}, B:{util.registers['B']}, C:{util.registers['C']}")
util.factory_defaults = (util.registers['A'], util.registers['B'], util.registers['C'])
util.instructions = instructions
print(f"instructions: {instructions}")

output = util.run()

print(','.join(output))

limits = util.findLimits()

util.findInstructionLimits(limits, len(instructions) -1)
util.getResults()

