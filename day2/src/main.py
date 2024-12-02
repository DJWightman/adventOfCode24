import os
import sys

def generateDeltas(report):
    deltas = [int(report[i]) - int(report[i-1]) for i in range(1, len(report))]
    sign = 1 if deltas[0] > 0 else -1
    return sign, deltas

def isLevelDeltaSafe(sign, level):
    if level == 0:
        return False
    if sign * level < 0:
        return False
    if abs(level) > 3:
        return False
    return True

def isReportSafe(report):
    sign, deltas = generateDeltas(report)
    for x in deltas:
        if isLevelDeltaSafe(sign, x) == False:
            return False
    return True

def main():
    use_exampleData = False

    if use_exampleData:
        fileName = "example.txt"
    else:
        fileName = "data.txt"

    dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    filePath = dir + "/../input/" + fileName
    inputFile = open(filePath, 'r')

    rows = []
    for line in inputFile:
        rows.append(line.replace('\n','').split(' '))

    safe_part1 = 0
    safe_part2 = 0
    for report in rows:
        if isReportSafe(report):
            safe_part1 += 1
        else:
            for i in range(len(report)):
                dampenedReport = [x for ii, x in enumerate(report) if ii != i]
                if isReportSafe(dampenedReport):
                    safe_part2 += 1
                    break
    
    print(f"Total part1 safe reports: {safe_part1}, dampened reports safe: {safe_part2}\r\nTotal part2 safe reports:{safe_part1 + safe_part2}")

if __name__ == "__main__":
    main()