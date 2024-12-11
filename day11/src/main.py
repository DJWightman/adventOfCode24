import sys
import os

P1_BLINK_COUNT = 25
P2_BLINK_COUNT = 75

from functools import cache
@cache
def blink(stone, depth):
    if depth == 0:
        return 1

    if stone == '0':
        ret = blink('1', depth -1)
    elif len(stone) % 2 == 0:
        splitLength = int(len(stone)/2)
        ret = blink(stone[:splitLength], depth - 1) + blink(str(int(stone[splitLength:])), depth - 1)
    else:
        ret = blink(str(int(stone)*2024), depth - 1)

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

part1 = 0
part2 = 0

for stone in stones:
    part1 += blink(stone, P1_BLINK_COUNT )
    part2 += blink(stone, P2_BLINK_COUNT)

print(f"num stones Part1: {part1} Part2: {part2}")


