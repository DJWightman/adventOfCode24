def printHello():
    print("hello")

def getObstructions(cube):
    obstructions = [[x,y] for y, row in enumerate(cube) for x, pos in enumerate(row) if pos == '#']
    return obstructions

def findStart(cube):
    start = [[x,y] for y, row in enumerate(cube) for x, pos in enumerate(row) if pos != '#' and pos != '.' ]
    if len(start) != 1:
        print("failed")
    return start[0]

def getCubePos(position, cube):
    return cube[position[1]][position[0]]

def getStartDirection(position, cube):
    start = getCubePos(position, cube)
    match start:
        case '^':
            return 0
        case '<':
            return 1
        case 'v':
            return 2
        case '>':
            return 3
        case _:
            return -1

def getLineInfo(position, direction, obstructions):
    index = 0 if direction%2 == 0 else 1
    temp = list(filter(lambda x: x[index] == position[index], obstructions))
    return position[index^1],[obstruction[index^1] for obstruction in temp]

def moveForward(position, direction, obstructions, max):
    ret = False
    linePos, lineObs = getLineInfo(position, direction, obstructions)
    lineObs.sort()
    if direction < 2:
        lineObs = list(filter(lambda x: x < linePos, lineObs))
        if len(lineObs):
            newlinePos = lineObs[-1] + 1
        else:
            newlinePos = 0
            ret = True
    else:
        lineObs = list(filter(lambda x: x > linePos, lineObs))
        if len(lineObs):
            newlinePos = lineObs[0] - 1
        else:
            newlinePos = max
            ret = True
    
    index = 1 if direction%2 == 0 else 0
    newPosition = [position[0], position[1]]
    newPosition[index] = newlinePos
    return newPosition, ret

def rotateRight(direction):
    direction = direction - 1 if direction != 0 else 3
    return direction
        

def calculateRouteLength_withoutLineCrossings(path):
    length = 0
    for i, pos in enumerate(path[1:], 1):
        diff = sum([abs(path[i-1][ii]-pos[ii]) for ii in range(2)])
        length += diff
        print(diff)
    return length

def drawLine(grid, p1, p2):
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    diff = abs(x)+abs(y)
    if x < 0 or y < 0:
        p1 = p2
    a = 0
    b = 0
    for i in range(diff + 1):
        if x == 0:
            a = i
        else:
            b = i
        grid[p1[1] - a][p1[0] - b] = 'X'



def calculateRouteLength(path, max):
    grid = [[' ' for i in range(max + 1)] for ii in range(max+1)]
    for i, pos in enumerate(path[1:], 1):
        drawLine(grid, path[i-1], path[i])
    length = 0
    for row in grid:
        for pos in row:
            if pos == 'X':
                length += 1
    return length
