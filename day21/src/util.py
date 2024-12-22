import heapq as hq
from functools import cache

keypad = (('7','8','9'),('4','5','6'), ('1','2','3'), ('','0','A'))
dirpad = (('','^', 'A'), ('<','v','>'))


def moveY(distance):
    if distance > 0:
        ret = distance * 'v'
    else:
        ret = (distance * -1) * '^'
    return ret

def moveX(distance):
    if distance > 0:
        ret = distance * '>'
    else:
        ret = (distance * -1) * '<'
    return ret

def getMoveCoords(c, pad):
    newPos = ()
    for y, r in enumerate(pad):
        if c in r:
            x = r.index(c)
            newPos = (x, y)
            break
    return newPos

def keypad_directions(code):
    start = (2,3)
    pos = start
    sequence = ''
    # print("keypad")
    for c in code:
        newPos = getMoveCoords(c, keypad)
        move = tuple(map(lambda a,b: a - b, newPos, pos))

        if move[1] > 0:
            s = moveX(move[0]) + moveY(move[1]) + 'A'
        else:
            s = moveY(move[1]) + moveX(move[0]) + 'A'

        sequence += s
        # print(newPos, move, s)
        pos = newPos

    return sequence

def getCodeNum(code):
    return int(code.replace('A',''))

def chainDirectional_old(code, chain):

    ks = code
    for i in range(chain):
        ks = dirpad_directions(ks)
    
    return ks


def dirpad_directions(char, start):
    
    newPos = getMoveCoords(char, dirpad)

    ret = ['','']
    # Go Y first
    mult = ((0,1), (1,0))

    for i, r in enumerate(ret):
        pos = start
        while pos != newPos:
            move = tuple(map(lambda a,b: a - b, newPos, pos))
            k = ((move[0] // abs(move[0]) if move[0] != 0 else 0),  (move[1] // abs(move[1])) if move[1]!= 0 else 0)
            print("move", move, k)
            if move[0] != 0 and move[1] != 0:
                mp = (pos[0] + (k[0] * mult[i][0]), pos[1] + (k[1]* mult[i][1]))
                if mp != (0,0):
                    ret[i] += (moveX(k[0]) * mult[i][0]) + (moveY(k[1]) * mult[i][1])
                else:
                    mp = (pos[0] + (k[0] * mult[i][1]), pos[1] + (k[1]* mult[i][0]))
                    ret[i] += (moveX(k[0]) * mult[i][1]) + (moveY(k[1]) * mult[i][0])

            elif move[1] != 0:
                mp = (pos[0], pos[1] + move[1])
                ret[i] += moveY(move[1])

            elif move[0] != 0:
                mp = (pos[0] + move[0], pos[1])
                ret[i] += moveX(move[0])

            pos = mp

        ret[i] += 'A'

    return ret

@cache
def chainDirectional(code, depth):

    if depth == 0:
        print("code", code, len(code))
        return len(code)

    pos = (2,0)

    ret = 0
    for c in code:
        ts = dirpad_directions(c, pos)
        print("ts", code, c, ts, pos)
        r1 = chainDirectional(ts[0], depth - 1)
        r2 = chainDirectional(ts[1], depth - 1)
        if r1 <= r2:
            ret += r1
        else:
            ret += r2
        pos = getMoveCoords(c, dirpad)
    print("ret", r1, r2, ret)
    return ret


def shortestPath(c, pos, chain):
    newPos = getMoveCoords(c, keypad)

    q = []
    seen = set()
    sequence = ''
    keySequence = ''
    hq.heappush(q, (len(sequence), keySequence, pos))

    directions = ((0,1), (0,-1), (1,0), (-1,0))


    while q:
        length, keySequence, pos = hq.heappop(q)

        if pos == newPos:
            return length, keySequence

        if pos in seen:
            continue

        seen.add(pos)

        move = tuple(map(lambda a,b: a - b, newPos, pos))

        if move[0] != 0 and move[1] != 0:
            if move[0] < 0:
                mp = tuple(map(lambda a, b: a + b, pos, directions[3]))
                if mp != (0,3):
                    ks = keySequence + moveX(-1)
                    l = chainDirectional(ks, chain)
                    hq.heappush(q,(l, ks, mp))

            elif move[0] > 0:
                mp = tuple(map(lambda a, b: a + b, pos, directions[2]))
                ks = keySequence + moveX(1)
                l = chainDirectional(ks, chain)
                hq.heappush(q,(l, ks, mp))

            if move[1] > 0:
                mp = tuple(map(lambda a, b: a + b, pos, directions[0]))
                if mp != (0,3):
                    ks = keySequence + moveY(1)
                    l = chainDirectional(ks, chain)
                    hq.heappush(q,(l, ks, mp))
            elif move[1] < 0:
                mp = tuple(map(lambda a, b: a + b, pos, directions[1]))
                ks = keySequence + moveY(-1)
                l = chainDirectional(ks, chain)
                hq.heappush(q,(l, ks, mp))
        
        elif move[0] != 0:
            move = tuple(map(lambda a,b: a - b, newPos, pos))
            ks = keySequence + moveX(move[0]) + 'A'
            l = chainDirectional(ks, chain)
            hq.heappush(q,(l, ks, newPos))
        else:
            move = tuple(map(lambda a,b: a - b, newPos, pos))
            ks = keySequence + moveY(move[1]) + 'A'
            l = chainDirectional(ks, chain)
            hq.heappush(q,(l, ks, newPos))
