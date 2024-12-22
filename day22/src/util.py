def part1(num):
    return ((num * 64) ^ num) % 16777216

def part2(num):
    return ((num // 32) ^ num) % 16777216

def part3(num):
    return ((num *2048) ^ num) % 16777216

def newSecretNumber(num):
    return part3(part2(part1(num)))