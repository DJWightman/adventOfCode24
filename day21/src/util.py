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

def dirpad_directions(code):
    start = (2,0)
    pos = start
    sequence = ''
    for c in code:
        newPos = getMoveCoords(c, dirpad)
        move = tuple(map(lambda a,b: a - b, newPos, pos))
        
        if move[1] > 0:
            s = moveY(move[1]) + moveX(move[0]) + 'A'
        else:
            s = moveX(move[0]) + moveY(move[1]) + 'A'
        sequence += s
        pos = newPos

    return sequence

def dirpad_directions2(code):
    start = (2,0)
    pos = start
    sequence = ''
    for c in code:
        newPos = getMoveCoords(c, dirpad)
        s = ''
        while pos != newPos:
            move = tuple(map(lambda a,b: a - b, newPos, pos))
            if move[1] != 0:
                dir = move[1] // abs(move[1])
                mp = (pos[0], pos[1] + dir)
                if mp != (0,0):
                    s += moveY(dir)
                    pos = mp
                else:
                    dir = move[0] // abs(move[0])
                    s += moveX(dir)
                    pos = (pos[0] + dir, pos[1])
            else:
                s += moveX(move[0])
                pos = newPos
        s += 'A'
        sequence += s

    return sequence

def dirpad_directions3(code):
    start = (2,0)
    pos = start
    sequence = ''
    for c in code:
        newPos = getMoveCoords(c, dirpad)
        s = ''
        while pos != newPos:
            move = tuple(map(lambda a,b: a - b, newPos, pos))
            if move[0] != 0:
                mp = (pos[0] + (move[0] // abs(move[0])), pos[1])
                if mp != (0,0):
                    s += moveX(move[0] // abs(move[0]))
                    pos = mp
                else:
                    s += moveY(move[1] // abs(move[1]))
                    pos = (pos[0], pos[1] + (move[1] // abs(move[1])))
            else:
                s += moveY(move[1])
                pos = newPos
        s += 'A'
        sequence += s

    return sequence

def dirpad_directions4(code, depth):
    start = (2,0)
    pos = start
    directions = ((0,1), (0,-1), (1,0), (-1,0))
    ret = 0
    for c in code:
        newPos = getMoveCoords(c, dirpad)
        move = tuple(map(lambda a,b: a - b, newPos, pos))
        l = [-1,-1,-1,-1,-1,-1]
        if move[0] != 0 and move[1] != 0:
            if move[0] < 0:
                mp = tuple(map(lambda a, b: a + b, pos, directions[3]))
                if mp != (0,0):
                    l[0] = chainDirectional(c, depth - 1)

            elif move[0] > 0:
                mp = tuple(map(lambda a, b: a + b, pos, directions[2]))
                l[1] = chainDirectional(c, depth -1)

            if move[1] > 0:
                mp = tuple(map(lambda a, b: a + b, pos, directions[0]))
                if mp != (0,0):
                    l[2] = chainDirectional(c, depth -1)
            elif move[1] < 0:
                mp = tuple(map(lambda a, b: a + b, pos, directions[1]))
                l[3] = chainDirectional(c, depth - 1)
        
        elif move[0] != 0:
            move = tuple(map(lambda a,b: a - b, newPos, pos))
            l[4] = chainDirectional(c, depth -1)
        else:
            move = tuple(map(lambda a,b: a - b, newPos, pos))
            l[5] = chainDirectional(c, depth - 1)
        
        print("Ls",l)
        while -1 in l:
            l[l.index(-1)] = max(l)
        ret += min(l)
    return ret


def getCodeNum(code):
    return int(code.replace('A',''))

def chainDirectional_old(code, chain):

    ks = code
    for i in range(chain):
        ks = dirpad_directions(ks)
    
    return ks


@cache
def chainDirectional(code, depth):

    ks0 = [x for x in dirpad_directions(code).replace('A', 'A,').split(',') if x]
    ks1 = [x for x in dirpad_directions2(code).replace('A', 'A,').split(',') if x]
    ks2 = [x for x in dirpad_directions3(code).replace('A', 'A,').split(',') if x]

    # print("lengths: ", len(''.join(ks0)),', ', len(''.join(ks1)),', ', len(''.join(ks2)))
    # ks = ks0 if len(''.join(ks0)) <= len(''.join(ks1)) else ks1
    # ks = ks if len(''.join(ks)) <= len(''.join(ks2)) else ks2
    # print("seqs: ", ''.join(ks),', ', ''.join(ks0),', ', ''.join(ks1),', ', ''.join(ks2))

    # print(code, ':', ks)
    if depth == 1:
        # ks = ks1 if len(''.join(ks1)) <= len(''.join(ks2)) else ks2
        ks = ks0 if len(''.join(ks0)) <= len(''.join(ks1)) else ks1
        ks = ks if len(''.join(ks)) <= len(''.join(ks2)) else ks2
        print("found: ", ks, len(''.join(ks)))
        return len(''.join(ks))
    
    start = (2,0)
    pos = start
    directions = ((0,1), (0,-1), (1,0), (-1,0))
    ret = 0
    for c in code:
        newPos = getMoveCoords(c, dirpad)
        while pos != newPos:
            move = tuple(map(lambda a,b: a - b, newPos, pos))
            l = [[-1,()],[-1,()]]
            if move[0] != 0 and move[1] != 0:
                if move[0] < 0:
                    mp = tuple(map(lambda a, b: a + b, pos, directions[3]))
                    if mp != (0,0):
                        ks = moveX(-1)
                        l[0] = (chainDirectional(ks, depth - 1), mp)

                elif move[0] > 0:
                    mp = tuple(map(lambda a, b: a + b, pos, directions[2]))
                    ks = moveX(1)
                    l[0] = (chainDirectional(ks, depth -1), mp)

                if move[1] > 0:
                    mp = tuple(map(lambda a, b: a + b, pos, directions[0]))
                    if mp != (0,0):
                        ks = moveY(1)
                        l[1] = (chainDirectional(ks, depth -1), mp)
                elif move[1] < 0:
                    mp = tuple(map(lambda a, b: a + b, pos, directions[1]))
                    ks = moveY(-1)
                    l[1] = (chainDirectional(ks, depth - 1), mp)
                
                if l[0][0] <= l[1][0] and l[0][0] != -1:
                    pos = l[0][1]
                    ret += l[0][0]
                else:
                    pos = l[1][1]
                    ret += l[1][0]
                print(pos)
                continue
            elif move[0] != 0:
                move = tuple(map(lambda a,b: a - b, newPos, pos))
                ks = moveX(move[0]) + 'A'
                l[0][0] = 0
                for k in ks:
                    l[0][0] += chainDirectional(k, depth -1)
                pos = newPos
            else:
                move = tuple(map(lambda a,b: a - b, newPos, pos))
                ks = moveY(move[1]) + 'A'
                l[1][0] = 0
                for k in ks:
                    l[1][0] = chainDirectional(k, depth - 1)
                pos = newPos
            
            l = [x for (x,y) in l]
            
            ret += max(l)

    return ret


def shortestPath(c, pos, chain):
    newPos = getMoveCoords(c, keypad)

    q = []
    seen = set()
    sequence = ''
    keySequence = ''
    hq.heappush(q, (len(sequence), sequence, keySequence, pos, [pos]))

    directions = ((0,1), (0,-1), (1,0), (-1,0))


    while q:
        length, sequence, keySequence, pos, path = hq.heappop(q)

        if pos == newPos:
            return sequence, keySequence

        if pos in seen:
            continue

        seen.add(pos)

        move = tuple(map(lambda a,b: a - b, newPos, pos))

        if move[0] != 0 and move[1] != 0:
            if move[0] < 0:
                mp = tuple(map(lambda a, b: a + b, pos, directions[3]))
                if mp != (0,3):
                    ks = keySequence + moveX(-1)
                    s = chainDirectional_old(ks, chain)
                    hq.heappush(q,(len(s), s, ks, mp, path + [mp]))

            elif move[0] > 0:
                mp = tuple(map(lambda a, b: a + b, pos, directions[2]))
                ks = keySequence + moveX(1)
                s = chainDirectional_old(ks, chain)
                hq.heappush(q,(len(s), s, ks, mp, path + [mp]))

            if move[1] > 0:
                mp = tuple(map(lambda a, b: a + b, pos, directions[0]))
                if mp != (0,3):
                    ks = keySequence + moveY(1)
                    s = chainDirectional_old(ks, chain)
                    hq.heappush(q,(len(s), s, ks, mp, path + [mp]))
            elif move[1] < 0:
                mp = tuple(map(lambda a, b: a + b, pos, directions[1]))
                ks = keySequence + moveY(-1)
                s = chainDirectional_old(ks, chain)
                hq.heappush(q,(len(s), s, ks, mp, path + [mp]))
        
        elif move[0] != 0:
            move = tuple(map(lambda a,b: a - b, newPos, pos))
            ks = keySequence + moveX(move[0]) + 'A'
            s = chainDirectional_old(ks, chain)
            hq.heappush(q,(len(s), s, ks, newPos, path + [newPos]))
        else:
            move = tuple(map(lambda a,b: a - b, newPos, pos))
            ks = keySequence + moveY(move[1]) + 'A'
            s = chainDirectional_old(ks, chain)
            hq.heappush(q,(len(s), s, ks, newPos, path + [newPos]))


def shortestPath2(c, pos, chain):
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
