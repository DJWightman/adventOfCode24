import sys
import os

def blink(stones):
    newStones = []
    for stone in stones:
        if stone == '0':
            newStone = ['1']
        elif len(stone) % 2 == 0:
            splitLength = int(len(stone)/2)
            newStone = [stone[:splitLength], str(int(stone[splitLength:]))]
        else:
            newStone = [str(int(stone)*2024)]
        
        newStones += newStone

    return newStones


use_exampleData = True

if use_exampleData:
    fileName = "example.txt"
else:
    fileName = "data.txt"

dir = os.path.dirname(os.path.abspath(sys.argv[0]))
filePath = dir + "/../input/" + fileName
inputFile = open(filePath, 'r')

stones = []
for line in inputFile:
    stones += line.replace('\n','').split(' ')

for i in range(25):
    print(f"blink: {i+1}")
    stones = blink(stones)
    print(f"num stones: {10*(len(stones)-1) + len(stones[-1])}")


