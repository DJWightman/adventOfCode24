move_key = { '^' : (0,-1), 'v' : (0, 1), '>' : (1,0), '<' : (-1,0)}

def insert_dot(grid, dot_pos):
    line = [x if i != dot_pos[0] else '.' for i, x in enumerate(grid[dot_pos[1]])]
    grid.pop(dot_pos[1])
    grid.insert(dot_pos[1], ''.join(line))

def move_vertical(grid, pos, m, item):
    c = grid[pos[1]][pos[0]]

    line = [x if i != pos[0] else item for i, x in enumerate(grid[pos[1]])]
    grid.pop(pos[1])
    grid.insert(pos[1], ''.join(line))
    
    if c == '.':
        return

    move_vertical(grid, (pos[0], pos[1] + m), m, c)

    if c == '@' or c == 'O':
        return

    if c == '[':
        move_vertical(grid, (pos[0] + 1, pos[1] + m), m, ']')
        insert_dot(grid, (pos[0] + 1, pos[1]))
    elif c == ']':
        move_vertical(grid, (pos[0] - 1, pos[1] + m), m, '[')
        insert_dot(grid,(pos[0] - 1, pos[1]))


def check_move_vertical(grid, pos, m):
    c = grid[pos[1]][pos[0]]
    match grid[pos[1]][pos[0]]:
        case '.':
            return True
        case '#':
            return False
        case '[':
            return check_move_vertical(grid, (pos[0], pos[1] + m), m) and check_move_vertical(grid, (pos[0] + 1, pos[1] + m), m)
        case ']':
            return check_move_vertical(grid, (pos[0], pos[1] + m), m) and check_move_vertical(grid, (pos[0] - 1, pos[1] + m), m)
        case 'O':
            return check_move_vertical(grid, (pos[0], pos[1] + m), m)
        case _:
            return False


def try_move_vertical(grid, d, sub):
    m = move_key[d][1]
    if check_move_vertical(grid, (sub[0], sub[1] + m), m):
        move_vertical(grid, (sub[0], sub[1]), m, '.')
        return True

    return False


def try_move_horizontal(grid, d, sub):
    m = move_key[d][0]
    p = sub[0]
    line = grid[sub[1]] 
    if (m < 0 and line[ line[:p].rfind('#') : p ].count('.') == 0 ) or ( m > 0 and line[p:line[p:].find('#') + p].count('.') == 0):
        return False

    dot_pos = line[:p].rfind('.') if m < 0 else line[p:].find('.') + p
    line = line[:dot_pos] + line[dot_pos + 1:]
    line = line[:p] + '.' + line[p:]
    grid.pop(sub[1])
    grid.insert(sub[1], ''.join(line))

    return True


def try_move_sub(grid, d, sub):
    move = move_key[d]
    if (move[0] == 0 and try_move_vertical(grid, d, sub)) or (move[1] == 0 and try_move_horizontal(grid, d, sub)):
        sub = tuple(map(lambda a, b: a + b, sub, move))
    return sub


def generate_part2_grid_and_sub(grid):
    part2_grid = []
    sub = (0,0)
    for i, r in enumerate(grid):
        nl = ''
        for ii, x in enumerate(r):
            match(x):
                case '#':
                    nl += '##'
                case 'O':
                    nl += "[]"
                case '.':
                    nl += '..'
                case '@':
                    nl += '@.'
                    sub = (2*ii, i)
        part2_grid.append(nl)
    return part2_grid, sub


def generate_gps(grid, c):
    gps = []
    for i, r in enumerate(grid):
        for ii, p in enumerate(r):
            if p == c:
                gps.append((i*100) + ii)

    return sum(gps)
