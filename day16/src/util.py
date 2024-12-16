
dir = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
reverse_dir =  {0: 2, 1: 3, 2: 0, 3: 1}
move = {dir['N']: (0,-1), dir['E']: (1,0), dir['S']: (0,1), dir['W']:(-1,0)}

def getSurroundings(grid, pos):
    S = grid[pos[1] + 1][pos[0]]
    N = grid[pos[1] - 1][pos[0]]
    E = grid[pos[1]][pos[0] + 1]
    W = grid[pos[1]][pos[0] - 1]
    return (N, E, S, W)

def rotateToDirection(heading, newHeading):
    multiplier = 1000
    diff = abs(heading - newHeading)
    match diff:
        case 0:
            return 0
        case 1:
            return multiplier
        case 3:
            return multiplier

def getNewData(score, path, position, heading, newHeading):

    

    return newScore, newPosition, newPath
