import sys
import os


def get_filename(use_exampleData):
    return "example.txt" if use_exampleData else "data.txt"     

def get_filepath(EXAMPLE_DATA):
    dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    return dir + "/../input/" + get_filename(EXAMPLE_DATA)
    return open(filePath, 'r')

