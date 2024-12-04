"""--- Day 4: Ceres Search ---
"Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the Ceres monitoring station!

As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:


..X...
.SAMX.
.A..A.
XMAS.S
.X....
The actual word search will be full of letters instead. For example:

MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not involved in any XMAS have been replaced with .:

....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
Take a look at the little Elf's word search. How many times does XMAS appear?"""

from collections import Counter

# def check_direction(direction: str, curr_char: str, position: tuple, dimensions: tuple, input, part_two=False):
#     col, row = position
#     col_max, row_max = dimensions
#     global count

#     if curr_char == 'X': next_char = 'M'
#     elif curr_char == 'M': next_char = 'A'
#     elif curr_char == 'A': next_char = 'S'
    
#     # print(f'curr_char: {curr_char}, direction: {direction}, position:{position}')

#     if direction == 'up':
#         if row == 0: return False
#         if input[row-1][col] == next_char:
#             if next_char == 'S': 
#                 count += 1
#                 return True
#             check_direction(direction='up', curr_char=next_char, position=(col, row-1), dimensions=(col_max, row_max), input=input)
#         else: return False

#     elif direction == 'upleft':
#         if row == 0 or col == 0: return False
#         if part_two: return input[row-1][col-1]
#         if input[row-1][col-1] == next_char:
#             if next_char == 'S': 
#                 count += 1
#                 return True
#             check_direction(direction='upleft', curr_char=next_char, position=(col-1, row-1), dimensions=(col_max, row_max), input=input)
#         else: return False

#     elif direction == 'upright':
#         if row == 0 or col == col_max: return False
#         if part_two: return input[row-1][col+1]
#         if input[row-1][col+1] == next_char:
#             if next_char == 'S': 
#                 count += 1
#                 return True
#             check_direction(direction='upright', curr_char=next_char, position=(col+1, row-1), dimensions=(col_max, row_max), input=input)
#         else: return False

#     elif direction == 'left':
#         if col == 0: return False
#         if input[row][col-1] == next_char:
#             if next_char == 'S': 
#                 count += 1
#                 return True
#             check_direction(direction='left', curr_char=next_char, position=(col-1, row), dimensions=(col_max, row_max), input=input)
#         else: return False

#     elif direction == 'right':
#         if col == col_max: return False
#         if input[row][col+1] == next_char:
#             if next_char == 'S': 
#                 count += 1
#                 return True
#             check_direction(direction='right', curr_char=next_char, position=(col+1, row), dimensions=(col_max, row_max), input=input)
#         else: return False

#     elif direction == 'down':
#         if row == row_max: return False
#         if input[row+1][col] == next_char:
#             if next_char == 'S': 
#                 count += 1
#                 return True
#             check_direction(direction='down', curr_char=next_char, position=(col, row+1), dimensions=(col_max, row_max), input=input)
#         else: return False

#     elif direction == 'downleft':
#         if row == row_max or col == 0: return False
#         if part_two: return input[row+1][col-1]
#         if input[row+1][col-1] == next_char:
#             if next_char == 'S': 
#                 count += 1
#                 return True
#             check_direction(direction='downleft', curr_char=next_char, position=(col-1, row+1), dimensions=(col_max, row_max), input=input)
#         else: return False

#     elif direction == 'downright':
#         if row == row_max or col == col_max: return False
#         if part_two: return input[row+1][col+1]
#         if input[row+1][col+1] == next_char:
#             if next_char == 'S': 
#                 count += 1
#                 return True
#             check_direction(direction='downright', curr_char=next_char, position=(col+1, row+1), dimensions=(col_max, row_max), input=input)
#         else: return False

# sample = 'day4sampleinput.txt'
# real = 'day4input.txt'

# with open(real, 'r') as file:
#     input = [list(line.strip()) for line in file]

#     dimensions = (len(input[0]) - 1, len(input) - 1)

#     directions = ['up', 'upleft', 'upright', 'left', 'right', 'down', 'downleft', 'downright']
#     count = 0
#     for y, row in enumerate(input):
#         for x, char in enumerate(row):
#             if char == 'X': 
#                 for direction in directions:
#                     check_direction(direction=direction, curr_char='X', position=(x, y), dimensions=dimensions, input=input)


    # print(count)

"""--- Part Two ---
The Elf looks quizzically at you. Did you misunderstand the assignment?

Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:

M.S
.A.
M.S
Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written forwards or backwards.

Here's the same example from before, but this time all of the X-MASes have been kept instead:

.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
In this example, an X-MAS appears 9 times.

Flip the word search from the instructions back over to the word search side and try again. How many times does an X-MAS appear?"""

# with open(real, 'r') as file:
#     input = [list(line.strip()) for line in file]

#     dimensions = (len(input[0]) - 1, len(input) - 1)

#     directions = ['upleft', 'upright', 'downleft', 'downright']
#     count = 0
#     for y, row in enumerate(input):
#         for x, char in enumerate(row):
#             if char == 'A':
#                 surrounding_letters = []
#                 for direction in directions: 
#                     surrounding_letters.append(check_direction(direction=direction, curr_char='A', position=(x, y), dimensions=dimensions, input=input, part_two=True))
#                 counted_letters = Counter(surrounding_letters)
#                 if counted_letters['M'] == 2 and counted_letters['S'] == 2 and input[y-1][x-1] != input[y+1][x+1]: 
#                     print(f'surrounding_letters: {surrounding_letters}', end="|")
#                     print(counted_letters)
#                     count += 1

#     print(count)

with open('day4input.txt', 'r') as file:
    input = [list(line.strip()) for line in file]
    DELTAS = [(dy, dx) for dy in (-1, 0, 1) for dx in (-1, 0, 1) if (dy, dx) != (0, 0)]
    XMAS = 'XMAS'
    L = len(XMAS)
    H, W = len(input), len(input[0])
    total = 0

    def is_within_bounds(row, col):
        return 0 <= row < H and 0 <= col < W

    # Part 1
    for row in range(H):
        for col in range(W):
            for (dy, dx) in DELTAS:
                match = True
                for i in range(L):
                    new_row, new_col = row + i * dy, col + i * dx
                    if not is_within_bounds(new_row, new_col) or input[new_row][new_col] != XMAS[i]:
                        match = False
                        break
                if match: total += 1

    # print(total)

    # Part 2
    DIAGONAL_DELTAS = [(dy, dx) for dy in (-1, 1) for dx in (-1, 1)]

    def check_diagonal_letters(row, col):
        return input[row-1][col-1] != input[row+1][col+1]

    def check_correct_letters(letters: dict):
        return letters['M'] == 2 and letters['S'] == 2   

    total = 0
    for row in range(H):
        for col in range(W):
            if input[row][col] == 'A':
                surrounding_letters = []
                for (dy, dx) in DIAGONAL_DELTAS:
                    new_row, new_col = row + dy, col + dx
                    if is_within_bounds(new_col, new_row): surrounding_letters.append(input[new_row][new_col])
                surrounding_letters_amount = Counter(surrounding_letters)

                if check_correct_letters(surrounding_letters_amount) and check_diagonal_letters(row, col): total += 1

    print(total)

