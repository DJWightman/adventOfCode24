def findCharLocations(grid, char):
    positions = [[x,y] for y, row in enumerate(grid) for x, pos in enumerate(row) if pos == char]
    return positions

def getLineVals(p0, p1):
    x = abs(p0 - p1)
    if p0 > p1:
        return [x, -x]
    return [-x, x]

def getOuterBounds(p0,p1):
    x = getLineVals(p0[0], p1[0])
    y = getLineVals(p0[1], p1[1])    
    return [[x[0], y[0]], [x[1], y[1]]]

def checkValue(pos, max, antinodes):
    if  (
            pos[0] >= 0 and pos[1] >= 0 and
            pos[0] <= max and pos[1] <= max
        ):
        if antinodes.count(pos) == 0:
            antinodes.append(pos)
        return True
    return False

def extendLine(point, slope, max, antinodes, part1):
    pos = [point[0] + slope[0], point[1] + slope[1]]
    while checkValue(pos, max, antinodes):
        if part1:
            break
        pos = [pos[0] + slope[0], pos[1] + slope[1]]

def getAntinodes(p0, points, max, antinodes, part1):
    for point in points:
        slopes = getOuterBounds(p0, point)
        if part1:
            extendLine(p0, slopes[0], max, antinodes, part1)
            extendLine(point, slopes[1], max, antinodes, part1) 
        else:
            extendLine(point, slopes[0], max, antinodes, part1)
            extendLine(p0, slopes[1], max, antinodes, part1)
