import os
import time
from .utils import *

def parse_into_2d_list(file_name: str)->list:
    with open(file_name, 'r') as f:
        return [list(line.strip()) for line in f.readlines()]

def get_2d_list_dimensions(lst: list)->tuple:
    """
    Returns (H, W)
    """
    return (len(lst), len(lst[0]))

def pprint_2d_list(lst: list, space=1, animate=False, delay=0.5):
    """
    Animating data only works if the dimensions of the 2D List is small enough to fit the terminal
    """
    if animate: os.system("cls" if os.name == "nt" else "clear")

    for row in lst:
        for element in row:
            print(element, end=' ' * space)
        print('\n', end='')

    if animate: time.sleep(delay)
