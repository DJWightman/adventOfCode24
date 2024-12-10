import sys
import os


def get_filename(use_exampleData):
    return "example.txt" if use_exampleData else "data.txt"     

def get_filepath(EXAMPLE_DATA):
    dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    return dir + "/../input/" + get_filename(EXAMPLE_DATA)
    return open(filePath, 'r')

def trailValue(trails, pos):
    return trails[pos[1]][pos[0]]

def posInRange(pos, length):
    return False if (pos[0] < 0 or pos[0] >= length or 
        pos[1] < 0 or pos[1] >= length) else True
        
