import os
import pyperclip
import requests

from aocd.get import current_day, most_recent_year
from aocd import get_data

sample_input_file = os.path.basename(__file__).split('.')[0] + 'sampleinput.txt'
input_file = os.path.basename(__file__).split('.')[0] + 'input.txt'

def create_token_file(session_id):
    # Don't forget to delete this line of code after calling it once to avoid pushing your session-id.
    user_dir = os.path.expanduser('~')
    file_path = user_dir + '\\.config\\aocd\\token'

    with open(file_path, 'w') as f:
        f.write(session_id)

def clipboard_input_file_names():
    print('code .\\' + sample_input_file, end='; ')
    print('code .\\' + input_file)
    pyperclip.copy('code .\\' + sample_input_file + '; code .\\' + input_file)
    
def create_input_files(year=most_recent_year(), day=current_day()):
    with open(sample_input_file, 'w') as file: pass

    print(f'day: {day}, year: {year}')
    with open(input_file, 'w') as file:
        file.write(get_data(day=day, year=year))

# create_input_files()
# clipboard_input_file_names()

# -------------------------------------------------------------------------------------------------------------------------------------------- #

with open(input_file, 'r') as f:
    input_grid = [list(line.strip()) for line in f.readlines()]

DIRECTIONS = {'^': (-1, 0), '<': (0, -1), '>': (0, 1), 'v': (1, 0)}
TURN = {'^': '>', '<': '^', '>': 'v', 'v': '<'}
H, W = len(input_grid), len(input_grid[0])
guard_info = dict()

def _is_within_bounds(row, col):
    return 0 <= row < H and 0 <= col < W

def _look_ahead(row, col, direction):
    if not _is_within_bounds(row=row + DIRECTIONS[direction][0], col=col + DIRECTIONS[direction][1]): return None
    # print(DIRECTIONS[direction])

    return input_grid[row + DIRECTIONS[direction][0]][col + DIRECTIONS[direction][1]]

def get_guard_position()->tuple:
    for i, row in enumerate(input_grid):
        for j, col in enumerate(row):
            if input_grid[i][j] in DIRECTIONS.keys():
                direction = input_grid[i][j]
                return (i, j, direction)
            
def move_guard(row, col, direction:str, part_two=False):
    global count
    global obstacles_amount
    global steps

    next_step = _look_ahead(row, col, direction)
    row_delta, col_delta = DIRECTIONS[direction]

    if next_step == '.' or next_step == 'X':
        if input_grid[row][col] == '.': 
            input_grid[row][col] = 'X'
            count += 1
        
        guard_info['row'] += row_delta
        guard_info['col'] += col_delta

        return True
    elif next_step == '#':
        guard_info['direction'] = TURN[direction]
        if part_two:
            if steps < STEPS_MAX:
                steps += 1
            else:
                print('Loop found.')
                obstacles_amount += 1
                steps = 0
                return None
        return True
    elif next_step is None:
        # Count the last step before exiting the map
        if part_two: steps = 0
        count += 1
        return None
    else:
        print('ERROR')

def reset():
    guard_info['row'] = default_guard_position['row']
    guard_info['col'] = default_guard_position['col']
    guard_info['direction'] = '^'
    input_grid[i][j] = '.'


count = 0   
guard_info['row'], guard_info['col'], guard_info['direction'] = get_guard_position()
default_guard_position = {'row': guard_info['row'], 'col': guard_info['col']}
input_grid[guard_info['row']][guard_info['col']] = 'X' # Since I'm storing the guard's location, I'm going to remove the guard on the map so it doesn't interfere with moving and checking elements
count += 1

# Part 1
# while move_guard(guard_info['row'], guard_info['col'], guard_info['direction']) is True: pass
# print(f'Count: {count}')

# Part 2
steps = 0
STEPS_MAX = 50000 # I put it to some really high number so I could just run this thing overnight haha
iterations = 0
input_grid[default_guard_position['row']][default_guard_position['col']] = '.'

obstacles_amount = 0
for i, row in enumerate(input_grid):
    for j, col in enumerate(input_grid):
        if input_grid[i][j] == '#': continue
        if i == default_guard_position['row'] and j == default_guard_position['col']: continue

        # print(f'{iterations}/{H*W} checked.', end=' | ')
        input_grid[i][j] = '#'
        # for line in input_grid: print(line)

        while move_guard(guard_info['row'], guard_info['col'], guard_info['direction'], part_two=True) is True: pass
        reset()
        iterations += 1

print(f'Obstacle Amount: {obstacles_amount}')