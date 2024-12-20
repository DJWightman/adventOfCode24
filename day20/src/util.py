import heapq as hq

def navigateGrid(grid, start, finish):

    q = []
    seen = []

    print("start:", start, " , finish:", finish)

    print(*grid, sep='\n')

    hq.heappush(q, (0, start, [start], [0]))
    directions = ((0,1), (0,-1), (1,0), (-1,0))
    gridsize = len(grid) - 1

    while q:
        moves, pos, path, ps = hq.heappop(q)

        if pos == finish or grid[pos[1]][pos[0]] == 'E':
            print(f"End path in {moves} picoseconds")
            ret = tuple([(a, ps[i]) for i, a in enumerate(path)])
            return ret

        if pos in seen:
            continue
        
        seen.append(pos)

        for d in directions:
            np = tuple(map(lambda a,b: a + b, pos, d))
            if np in path:
                continue
            if 0 < np[0] < gridsize and 0 < np[1] < gridsize and grid[np[1]][np[0]] != '#':
                hq.heappush(q,(moves + 1, np, path + [np], ps + [moves + 1]))
    
    return ()

def findPart1ShortCuts(shortestPath):

    shortcuts = []
    for (s, st) in shortestPath:
        for (f, ft) in shortestPath:
            if s == f:
                continue

            if (ft - st > 2 and ((abs(s[0] - f[0]) == 2 and s[1] == f[1]) or
                (abs(s[1] - f[1]) == 2 and s[0] == f[0]))):
                shortcuts.append((ft - st - 2, s,f))
    
    return shortcuts


def findShortcuts(grid, spath, start):

    q = []
    seen = []
    shortCuts = []
    tspath = [p for (p,t) in spath]

    hq.heappush(q, (0, start, [start]))
    directions = ((0,1), (0,-1), (1,0), (-1,0))
    gridsize = len(grid) - 1

    while q:
        moves, pos, path = hq.heappop(q)

        if moves > 20:
            break

        if pos in seen:
            continue
        
        seen.append(pos)
        
        if pos[0] in tspath:
            (f, ft) = pos
            (s, st) = start
            (ts, tst) = spath[tspath.index(pos[0])]
            if (ft - st) > (ft - tst):
                shortCuts.append((ft - st - 2, s,f))

        for d in directions:
            np = tuple(map(lambda a,b: a + b, pos[0], d))
            if np in path:
                continue
            if 0 < np[0] < gridsize and 0 < np[1] < gridsize:
                hq.heappush(q,(moves + 1, (np, start[1] + moves + 1), path + [np]))
    
    return shortCuts