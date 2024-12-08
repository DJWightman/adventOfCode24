def findCharLocations(grid, char):
    positions = [[x,y] for y, row in enumerate(grid) for x, pos in enumerate(row) if pos == char]
    return positions

def getOuterBounds(p0,p1):
    x = abs(p0 - p1)
    if p0 > p1:
        return [p0 + x, p1 - x]
    return [p0 -x, p1 + x]

def getAntinodes(p0, points, max, _antinodes):
    antinodes = []
    for point in points:
        xs = getOuterBounds(p0[0], point[0])
        ys = getOuterBounds(p0[1], point[1])
        bmin = [xs[0], ys[0]]
        bmax = [xs[1], ys[1]]
        if  (
                xs[0] >= 0 and ys[0] >= 0 and
                xs[0] <= max and ys[0] <= max and
                _antinodes.count(bmin) == 0
            ):
            antinodes.append(bmin)
        if  (
                xs[1] >= 0 and ys[1] >= 0 and
                xs[1] <= max and ys[1] <= max and
                _antinodes.count(bmax) == 0
            ):
            antinodes.append(bmax)
        
    return antinodes
