import sys
import os
import util
import time

cache = {}
cache2 = {}

solved = False

def recursive(target, nums, part2):
    global solved
    if len(nums) == 1:
        if target == nums[0]:
            solved = True
            return 1
        else:
            return 0

    if nums[0] > target or solved:
        return 0

    ret = 0
    if recursive(target, [nums[0] * nums[1]] + nums[2:], part2) == 1 or recursive(target, [nums[0] + nums[1]] + nums[2:], part2) == 1:
        ret = 1
    elif part2:
        ret = recursive(target, [util.concat(nums[0], nums[1])] + nums[2:], part2)
    else:
        ret = 0

    return ret
    

start_time = time.time()
use_exampleData = False

if use_exampleData:
    fileName = "example.txt"
else:
    fileName = "data.txt"

dir = os.path.dirname(os.path.abspath(sys.argv[0]))
filePath = dir + "/../input/" + fileName
inputFile = open(filePath, 'r')

rows = []
total_part1 = 0
total_part2 = 0

for line in inputFile:
    target, nums = line.replace('\n','').split(': ')
    target = int(target)
    nums = list(map(int, nums.split(' ')))
    total_part1 += target * recursive(target, nums, False)
    solved = False
    total_part2 += target * recursive(target, nums, True)
    solved = False

print(total_part1)
print(total_part2)
print(f"total time to execute: {time.time() - start_time}")