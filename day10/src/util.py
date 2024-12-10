directions = ((1,0), (-1,0), (0,1), (0,-1))

def findPath(trails, pos, trailPaths):
    max = len(trails)
    currentVal = trails[pos[1]][pos[0]]
    ret = [0,0]
    if currentVal == 9:
        ret[1] = 1
        if pos not in trailPaths:
            trailPaths.append(tuple(pos))
            ret[0] = 1
            return ret
        return ret

    for d in directions:
        x = pos[0] + d[0]
        y = pos[1] + d[1]
        if (x not in [a for a in range(max)] or
            y not in [a for a in range(max)] ):
            continue
        if  trails[y][x] - currentVal == 1:
            ret = list(map(lambda x,y: x + y, ret, findPath(trails, (x, y), trailPaths)))   
    return ret