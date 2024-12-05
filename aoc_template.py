import os
import pyperclip
import requests

from aocd.models import default_user, Puzzle, User
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

def get_current_session_id():
    # Expires January 6th, 2026
    with open('session_id.txt', 'r') as f:
        return f.read()

def create_input_files(year=most_recent_year(), day=current_day()):
    with open(sample_input_file, 'w') as file: pass

    print(f'day: {day}, year: {year}')
    with open(input_file, 'w') as file:
        file.write(get_data(day=day, year=year))

# create_input_files()
# clipboard_input_file_names()


with open('aoc_template.py', 'w') as f: pass