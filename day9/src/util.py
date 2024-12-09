
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
        print(f"test: {i}")
        if decoded[i] != '.':
            return i
    return -1

def defragData(decoded):
    lastIndex = getLastIndex(decoded)
    print(f"len: {len(decoded)} lI: {lastIndex}")

    for i in range(len(decoded)):
        if decoded[i] != '.':
            print(f"num: {decoded[i]} i: {i}")
            continue
        
        if i >= lastIndex:
            return

        #print(decoded)
        decoded[i] = decoded[lastIndex]
        decoded[lastIndex] = '.'
        lastIndex = getLastIndex(decoded[:lastIndex])
        print(f"i: {i} last: {lastIndex}")

def computeChecksum(decoded):
    checksum = 0
    for i, num in enumerate(decoded):
        if num == '.':
            break
        checksum += i * num

    return checksum
