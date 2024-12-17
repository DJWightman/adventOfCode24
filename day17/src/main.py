import os
import sys
import util
import program

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
            RegA = int(a)
        case "Register B":
            RegB = int(a)
        case "Register C":
            RegC = int(a)
        case "Program":
            instructions = tuple([int(x) for x in a.split(',')])
        case _:
            continue

print(f"Registers A:{RegA}, B:{RegB}, C:{RegC}")
program.setRegisters(RegA, RegB, RegC)
program.setInstructions(instructions)
print(f"instructions: {instructions}")

output = program.run()


print("part1 results: ", ','.join(output))

min = 0
for i in reversed(range(program.programLength())):
    t = 0
    while 1:
        RegA = (min << 3) + t
        if program.verify2(RegA, i):
            min = RegA
            break
        t += 1
print(f"part2 solution: {min}")

