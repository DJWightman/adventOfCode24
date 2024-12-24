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
