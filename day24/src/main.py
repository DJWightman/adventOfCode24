import os
import sys

use_exampleData = False
if use_exampleData:
    fileName = "example1.txt"
else:
    fileName = "data.txt"

dir = os.path.dirname(os.path.abspath(sys.argv[0]))
filePath = dir + "/../input/" + fileName
inputFile = open(filePath, 'r')

inputs = {}
puzzles = []
answer = 0
for line in inputFile:
    temp = line.replace('\n','').split(' ')

    if len(temp) == 2:
        inputs[temp[0].replace(':', '')] = int(temp[1])
    
    elif len(temp) == 5:
        puzzles += [(temp[0], temp[2], temp[1], temp[-1])]
        # match temp[1]:
        #     case "AND":
        #         outputs[temp[-1]] = inputs[temp[0]] & inputs[temp[2]]
        #     case "OR":
        #         outputs[temp[-1]] = inputs[temp[0]] | inputs[temp[2]]
        #     case "XOR":
        #         outputs[temp[-1]] = inputs[temp[0]] ^ inputs[temp[2]]
        
        # if temp[-1][0] == 'z':
        #     t = outputs[temp[-1]] << int(temp[-1][1:])   
        #     answer += t
        #     print(temp[-1], temp[-1][1:], t)      

print(puzzles)

orig_puzzles = puzzles.copy()


while puzzles:
    for p in puzzles:
        if p[0] in inputs and p[1] in inputs:
            match p[2]:
                case "AND":
                    inputs[p[3]] = inputs[p[0]] & inputs[p[1]]
                case "OR":
                    inputs[p[3]] = inputs[p[0]] | inputs[p[1]]
                case "XOR":
                    inputs[p[3]] = inputs[p[0]] ^ inputs[p[1]]
            
            if p[3][0] == 'z':
                t = inputs[p[3]] << int(p[3][1:])   
                answer += t
            puzzles.remove(p)

print(inputs)

print(answer)

# All XOR gates must include x##, y##, or z##

# Except for z45, no OR gates can have z## as an output

# No AND gates can have z## as an output

# Except for z00, the output of x## XOR y## must be the input to another XOR gate

# Except for x00 AND y00, the output of an AND gate must be the input to an OR gate


bad_gates = []

# print("here", orig_puzzles)
for p in orig_puzzles:

    match p[2]:
        case "XOR":
            if (p[0][0] in 'xy' and p[1][0] in 'xy'):
                if p[3] == 'z00':
                    continue
                test_out =  list(set([p[3] for p1 in orig_puzzles if (p[3] == p1[0] or p[3] == p1[1]) and p1[2] == 'XOR']))
                if not test_out:
                    print("herpy", p[3])
                    bad_gates += [(p[3], "rule1")]
            elif p[3][0] == 'z':
                continue
            else:
                bad_gates += [(p[3], "rule2")]
        case "AND":
            if  p[3][0] == 'z':
                bad_gates += [(p[3], "rule3")]
            elif p[0][0] in 'xy' and p[0][1:] == '00':
                continue
            else:
                test_out = list(set([p[3] for p1 in orig_puzzles if (p[3] == p1[0] or p[3] == p1[1]) and p1[2] != 'OR']))
                if test_out:
                    bad_gates += [(p[3], "rule4")]

        case "OR":
            if p[3][0] != 'z' or p[3][1:] == '45':
                continue
            bad_gates += [(p[3], "rule5")]

print("derp", bad_gates, len(bad_gates))

print(','.join(sorted([x for x,y in bad_gates])))

