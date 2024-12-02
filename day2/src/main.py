import os
import sys

def isSafe(report):
    deltas = [int(report[i]) - int(report[i-1]) for i in range(1, len(report))]
    #print(deltas)
    sign = deltas[0]
    for x in deltas:
        if x == 0:
            return False
        if sign * x < 0:
            return False
        if abs(x) > 3:
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

    #print(rows)
    safe = 0
    for report in rows:
        if isSafe(report):
            #print("Safe")
            safe += 1
        # else:
        #     print("Unsafe")
    
    print(f"Total safe: {safe}")

if __name__ == "__main__":
    main()