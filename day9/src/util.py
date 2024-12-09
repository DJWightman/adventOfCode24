
key = {"id": 0, "length": 1}

def decodeLine(line):
    decoded = []
    data = True
    id = 0
    for char in line:
        num = int(char)
        if data:
            decoded += [id for i in range(num)]
            id += 1
            data = False
        else:
            decoded += ['.' for i in range(num)]
            data = True
    
    return decoded


def getLastIndex(decoded):
    for i in reversed(range(len(decoded))):
        if decoded[i] != '.':
            return i
    return -1

def defragData(decoded):
    lastIndex = getLastIndex(decoded)
    part1 = []
    print(f"len: {len(decoded)} lI: {lastIndex}")

    for i in range(len(decoded)):
        if i > lastIndex:
            break

        if decoded[i] != '.':
            part1.append(decoded[i])
            continue   


        part1.append(decoded[lastIndex])
        lastIndex = getLastIndex(decoded[:lastIndex])
    
    return part1


def computeChecksum(decoded):
    checksum = 0
    for i, num in enumerate(decoded):
        if num == '.':
            continue
        checksum += i * num

    return checksum


def doubleDecode(data):
    match = data[0]
    decode2 = [[match, 1]]
    for x in data[1:]:
        if x == match:
            decode2[-1][1] += 1
        else:
            match = x
            decode2.append([match,1])
    
    return decode2

def findLastData(data, target):
    if target == 0:
        return False, [-1,-1]

    for i in reversed(range(len(data))):
        if data[i][0] != '.' and data[i][1] <= target:
            return True, i
    return False, [-1,-1]


def defrag2(data):
    part2 = []

    i = len(data) - 1
    while i > 0:
        x = data[i]
        if x[0] == '.':
            i -= 1
            continue

        for ii, y in enumerate(data):
            if ii >= i:
                break
            if y[0] != '.':
                continue
            if y[1] < x[1]:
                continue

            temp1 = ['.', x[1]]
            temp2 = ['.', y[1] - x[1]]
            data.pop(ii)
            data.insert(ii, x)
            data.pop(i)
            data.insert(i, temp1)
            if y[1] > x[1]:
                data.insert(ii+1, temp2)
                i += 1

            break
        i -= 1

    for x in data:
        part2 += [x[0] for i in range(x[1])]
    return part2

