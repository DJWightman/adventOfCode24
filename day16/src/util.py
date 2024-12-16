def getSurroundings(grid, pos):
    S = grid[pos[1] + 1][pos[0]]
    N = grid[pos[1] - 1][pos[0]]
    E = grid[pos[1]][pos[0] + 1]
    W = grid[pos[1]][pos[0] - 1]
    return (N, E, S, W)

def rotateToDirection(heading, direction):
    multiplier = 1000
    diff = abs(heading - direction)
    match diff:
        case 0:
            return 0
        case 1:
            return multiplier
        case 2:
            return multiplier * 2
        case 3:
            return multiplier