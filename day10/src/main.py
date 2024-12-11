import util
EXAMPLE_DATA = 0
TRAIL_HEAD = 0
TRAIL_PEAK = 9

def getScore(pos, trailPaths):
    ret = {"part1": 0, "part2": 0 }
    if pos not in trailPaths:
        trailPaths.append(tuple(pos))
        ret["part1"] = 1
    ret["part2"] = 1
    return ret

def findPath(trails, pos, trailPaths):
    if util.trailValue(trails, pos) == TRAIL_PEAK:
        return getScore(pos, trailPaths)

    ret = {"part1": 0, "part2": 0 }
    directions = ((1,0), (-1,0), (0,1), (0,-1))
    for offset in directions:
        newPos = tuple(map(lambda x, y: x + y, pos, offset))
        if ( util.posInRange(newPos, len(trails)) and
             util.trailValue(trails, newPos) - util.trailValue(trails, pos) == 1 ):
            # Add return values of recursive findPath() 
            # for Part 1 and Part 2 to the return dictionary
            for key, value in findPath(trails, newPos, trailPaths).items():
                ret[key] += value
    return ret

def main():
    trails = tuple(
            [tuple([int(x) for x in line.replace('\n','')]) 
                for line in open(util.get_filepath(EXAMPLE_DATA), 'r')]
        )

    trailheads = [ (x , y)
                    for y, row in enumerate(trails) 
                        for x, val in enumerate(row) if val == TRAIL_HEAD
                ]

    scores = {"part1": 0, "part2": 0 }
    for trailhead in trailheads:
        trailPaths = []
        for key, value in findPath(trails, trailhead, trailPaths).items():
            scores[key] += value

    print(f"total sum: {scores["part1"]}")
    print(f"total P2 sum: {scores["part2"]}")

if __name__ == "__main__":
    main()
