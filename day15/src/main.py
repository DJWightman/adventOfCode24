import os
import sys


use_exampleData = False
if use_exampleData:
    fileName = "example.txt"
else:
    fileName = "data.txt"

dir = os.path.dirname(os.path.abspath(sys.argv[0]))
filePath = dir + "/../input/" + fileName
inputFile = open(filePath, 'r')

grid = []
directions = ''
sub = (0,0)
for line in inputFile:
    if line[0] == '#':
        if '@' in line:
            sub = (line.index('@'), len(grid))
        grid.append(line.replace('\n',''))
    else:
        directions += line.replace('\n','')

print(*grid,sep='\n')

print(directions)
print(sub)

move_key = { '^' : (0,-1), 'v' : (0, 1), '>' : (1,0), '<' : (-1,0)}

for d in directions:

    move = move_key[d]
    op = sub[0] if move[0] == 0 else sub[1]
    p = sub[0] if move[0] != 0 else sub[1]
    line = ''.join([r[op] for r in grid]) if move[0] == 0 else grid[op] 
    m = move[1] if move[0] == 0 else move[0]

    if (m < 0 and line[ line[:p].rfind('#') : p ].count('.') == 0 ) or ( m > 0 and line[p:line[p:].find('#') + p].count('.') == 0):
        continue

    dot_pos = line[:p].rfind('.') if m < 0 else line[p:].find('.') + p
    al = [x for x in line]
    al.pop(dot_pos)
    al.insert(p, '.')
    sub = tuple(map(lambda a, b: a + b, sub, move))
    if move[0] == 0:
        for i, r in enumerate(grid):
            ar = [x for x in r]
            ar[op] = al[i]
            grid.pop(i)
            grid.insert(i, ''.join(ar))
    else:
        grid.pop(op)
        grid.insert(op, ''.join(al))
    
print(*grid,sep='\n')
print()


gps = []
for i, r in enumerate(grid):
    for ii, p in enumerate(r):
        if p == 'O':
            gps.append((i*100) + ii)

print(sum(gps))