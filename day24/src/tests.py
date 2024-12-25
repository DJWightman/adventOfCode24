import util

def test_all_0_except_main_ones(puzzles, main_roots, root_sets, out):

    roots = {}
    for r in root_sets:
        roots[r[0]] = 0
        roots[r[1]] = 0
    roots[main_roots[0]] = 1
    roots[main_roots[1]] = 1

    return util.solvePuzzle(puzzles, roots, out) == 1

def test_all_1_except_main_zeroes(puzzles, main_roots, root_sets, out):

    roots = {}
    for r in root_sets:
        roots[r[0]] = 1
        roots[r[1]] = 1
    roots[main_roots[0]] = 0
    roots[main_roots[1]] = 0

    return util.solvePuzzle(puzzles, roots, out) == 0

def test_all_1(puzzles, main_roots, root_sets, out):

    roots = {}
    for r in root_sets:
        roots[r[0]] = 1
        roots[r[1]] = 1

    return util.solvePuzzle(puzzles, roots, out) == 1

def test_all_0(puzzles, main_roots, root_sets, out):

    roots = {}
    for r in root_sets:
        roots[r[0]] = 0
        roots[r[1]] = 0

    return util.solvePuzzle(puzzles, roots, out) == 0

def test_all_0_main_xor(puzzles, main_roots, root_sets, out):

    roots = {}
    for r in root_sets:
        roots[r[0]] = 0
        roots[r[1]] = 0
    roots[main_roots[0]] = 0
    roots[main_roots[1]] = 1
    ret = util.solvePuzzle(puzzles, roots, out) == 0

    for r in root_sets:
        roots[r[0]] = 0
        roots[r[1]] = 0
    roots[main_roots[0]] = 1
    roots[main_roots[1]] = 0
    return ret and util.solvePuzzle(puzzles, roots, out) == 0

def test_all_1_main_xor(puzzles, main_roots, root_sets, out):

    roots = {}
    for r in root_sets:
        roots[r[0]] = 1
        roots[r[1]] = 1
    roots[main_roots[0]] = 0
    roots[main_roots[1]] = 1
    ret = util.solvePuzzle(puzzles, roots, out) == 0

    for r in root_sets:
        roots[r[0]] = 1
        roots[r[1]] = 1
    roots[main_roots[0]] = 1
    roots[main_roots[1]] = 0
    return ret and util.solvePuzzle(puzzles, roots, out) == 0

def test_all_xor_main_1(puzzles, main_roots, root_sets, out):

    roots = {}
    for r in root_sets:
        roots[r[0]] = 0
        roots[r[1]] = 1
    roots[main_roots[0]] = 1
    roots[main_roots[1]] = 1
    ret = util.solvePuzzle(puzzles, roots, out) == 1

    for r in root_sets:
        roots[r[0]] = 1
        roots[r[1]] = 0
    roots[main_roots[0]] = 1
    roots[main_roots[1]] = 1
    return ret and util.solvePuzzle(puzzles, roots, out) == 1

def test_all_xor_main_0(puzzles, main_roots, root_sets, out):

    roots = {}
    for r in root_sets:
        roots[r[0]] = 0
        roots[r[1]] = 1
    roots[main_roots[0]] = 0
    roots[main_roots[1]] = 0
    ret = util.solvePuzzle(puzzles, roots, out) == 0

    for r in root_sets:
        roots[r[0]] = 1
        roots[r[1]] = 0
    roots[main_roots[0]] = 0
    roots[main_roots[1]] = 0
    return ret and util.solvePuzzle(puzzles, roots, out) == 0

def test_all_xor(puzzles, main_roots, root_sets, out):

    roots = {}
    for r in root_sets:
        roots[r[0]] = 0
        roots[r[1]] = 1
    roots[main_roots[0]] = 0
    roots[main_roots[1]] = 1
    ret = util.solvePuzzle(puzzles, roots, out) == 0

    for r in root_sets:
        roots[r[0]] = 1
        roots[r[1]] = 0
    roots[main_roots[0]] = 1
    roots[main_roots[1]] = 0
    return ret and util.solvePuzzle(puzzles, roots, out) == 0
