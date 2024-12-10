import util
EXAMPLE_DATA = 0

def findPath(trails, pos, trailPaths):
    ret = {"part1": 0, "part2": 0 }

    if util.trailValue(trails, pos) == 9:
        if pos not in trailPaths:
            trailPaths.append(tuple(pos))
            ret["part1"] = 1
        ret["part2"] = 1
        return ret

    directions = ((1,0), (-1,0), (0,1), (0,-1))
    for offset in directions:
        newPos = tuple(map(lambda x, y: x + y, pos, offset))

        if not util.posInRange(newPos, len(trails)):
            continue

        if  util.trailValue(trails, newPos) - util.trailValue(trails, pos) == 1:
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
                        for x, val in enumerate(row) if val == 0
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
