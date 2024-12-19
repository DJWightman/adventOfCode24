import heapq as hq

def navigateGrid(fd, GRID_SIZE):

    grid = [['#' if (ii,i) in fd else '.' for ii in range(GRID_SIZE)] for i in range(GRID_SIZE)]
    q = []
    seen = []

    hq.heappush(q, (0, (0,0), [(0,0)]))
    directions = ((0,1), (0,-1), (1,0), (-1,0))

    while q:
        moves, pos, path = hq.heappop(q)

        if pos[0] == GRID_SIZE - 1 and pos[1] == GRID_SIZE - 1:
            return moves

        if pos in seen:
            continue
        
        seen.append(pos)

        for d in directions:
            np = tuple(map(lambda a,b: a + b, pos, d))
            if 0 <= np[0] < GRID_SIZE and 0 <= np[1] < GRID_SIZE and grid[np[1]][np[0]] == '.':
                hq.heappush(q,(moves + 1, np, path + [np]))
    
    return -1


def findFirstPosition(low, high, data, size):

    mid = (high + low) // 2

    moves = navigateGrid(data[:mid],size)
    if mid == low:
        print("Part2:")
        if moves == -1:
            print("found at: ", mid,", point: ", data[mid])
            return mid
        print("found at: ", high,", point: ", data[mid])
        return high
    
    if moves == -1:
        return findFirstPosition(low, mid, data, size)
    return findFirstPosition(mid, high, data, size)
