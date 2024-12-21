import heapq as hq
from functools import cache

def navigateGrid(grid, start, finish):

    q = []
    seen = []

    print("start:", start, " , finish:", finish)

    print(*grid, sep='\n')

    hq.heappush(q, (0, start, [start]))
    directions = ((0,1), (0,-1), (1,0), (-1,0))
    gridsize = len(grid) - 1

    while q:
        moves, pos, path = hq.heappop(q)

        if pos == finish or grid[pos[1]][pos[0]] == 'E':
            print(f"End path in {moves} picoseconds")
            return tuple(path)

        if pos in seen:
            continue
        
        seen.append(pos)

        for d in directions:
            np = tuple(map(lambda a,b: a + b, pos, d))
            if grid[np[1]][np[0]] == '#' or np in path or np in seen:
                continue
            if 0 < np[0] < gridsize and 0 < np[1] < gridsize:
                hq.heappush(q,(moves + 1, np, path + [np]))
    
    return ()

def navGrid(grid, start, finish):
    directions = ((0,1), (0,-1), (1,0), (-1,0))
    # print(*grid, sep='\n')
    pos = start
    path = [start]
    while pos != finish:
        for d in directions:
            np = tuple(map(lambda a,b: a + b, pos, d))
            if np not in path and grid[np[1]][np[0]] != '#':
                pos = np
                path += [np]
                break
    
    return path


def findPart1ShortCuts(shortestPath):

    shortcuts = []
    for si in range(len(shortestPath)):
        for fi in range(len(shortestPath)):
            if shortestPath[si] == shortestPath[fi]:
                continue
            s = shortestPath[si]
            f = shortestPath[fi]
            if (fi - si > 2 and ((abs(s[0] - f[0]) == 2 and s[1] == f[1]) or
                (abs(s[1] - f[1]) == 2 and s[0] == f[0]))):
                shortcuts.append((fi - si - 2, s,f))
    
    return shortcuts


def findIndexShortcuts(grid, spath, start_index, allowedMoves, target):
    directions = ((0,1), (0,-1), (1,0), (-1,0))
    gridsize = len(grid) - 1

    q = []
    seen = set()
    shortCuts = []
    start = spath[start_index]
    hq.heappush(q, (0, start, [start]))

    while q:
        moves, pos, path = hq.heappop(q)

        if moves > allowedMoves:
            break

        if pos in seen:
            continue
        
        seen.add(pos)
        
        if pos != start and pos in spath:
            finish_index = spath.index(pos)
            finish = spath[spath.index(pos)]
            savings = finish_index - start_index - moves
            if savings >= target:
                shortCuts.append((savings, start_index, finish_index))


        for d in directions:
            np = tuple(map(lambda a,b: a + b, pos, d))
            if np in path or np in seen:
                continue
            if 0 < np[0] < gridsize and 0 < np[1] < gridsize:
                # print("here", np)
                hq.heappush(q,(moves + 1, np, path + [np]))
    
    return shortCuts


def findShortcuts(grid, spath, allowedMoves, target):
    ret = []
    i = 0
    for index in range(len(spath)):
        print("Checking index: ", index)
        ret += findIndexShortcuts(grid, spath, index, allowedMoves, target)

    return ret

def findShortcuts2(grid, spath, allowedMoves, target):
    ret = []
    for i, start in enumerate(spath[:-target]):
        for ii, end in enumerate(spath[i + target:], i + target):
            moves = sum(list(map(lambda a, b: abs(a - b), end, start)))
            if moves > allowedMoves:
                continue
            savings = ii - i - moves
            if savings < target:
                continue
            
            ret.append((savings, i, ii))
    
    return ret
