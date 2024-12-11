import sys
import os

BLINK_COUNT = 75

cache = {}

def blink(stone, depth):
    if depth == 0:
        return 1
    
    item = (stone, depth)
    print(item)
    if item in cache:
        return cache[item]

    if stone == '0':
        ret = blink('1', depth -1)
    elif len(stone) % 2 == 0:
        splitLength = int(len(stone)/2)
        ret = blink(stone[:splitLength], depth - 1) + blink(str(int(stone[splitLength:])), depth - 1)
    else:
        ret = blink(str(int(stone)*2024), depth - 1)
    
    cache[item] = ret

    return ret


use_exampleData = False

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

count = 0
for stone in stones:
    count += blink(stone, BLINK_COUNT )

print(f"num stones: {count}")


