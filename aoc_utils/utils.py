import os
import inspect
from pprint import pprint

from .list_utils import *

def debug_print(*args):
    """
    Pretty prints the variable name and it's content(s) for debugging.
    """
    callers_local_vars = inspect.currentframe().f_back.f_locals
    arg_names = [name for name, value in callers_local_vars.items() if value in args]

    for arg, arg_name in zip(args, arg_names):
        if type(arg) == list:
            print(f"{arg_name}: \n{pprint_2d_list(arg)}")
        elif type(arg) == dict:
            print(f"{arg_name}: \n{pprint(arg)}")
        else:
            print(f"{arg_name}: {arg}")

def get_deltas(directions='all'):
    """
    Returns the possible deltas for movement within a 2D list.
    """
    if directions == 'all':
        return tuple((dy, dx) for dy in (-1, 0, 1) for dx in (-1, 0, 1) if (dy, dx) != (0, 0))
    elif directions == 'diagonal':
        return tuple((dy, dx) for dy in (-1, 1) for dx in (-1, 1))
    elif directions == 'adjacent':
        return ((-1, 0), (1, 0), (0, -1), (0, 1))
    else:
        assert False, 'Invalid Direction Key.'
    
def create_dict(keys: list|tuple, values: list|tuple)->dict:
    """
    QoL for creating dictionaries if the keys and values are already on hand.
    """
    return {key: value for key, value in zip(keys, values)}
