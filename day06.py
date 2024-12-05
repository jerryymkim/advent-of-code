import os
import pyperclip
import requests

from aocp import (
    IntParser, 
    ListParser, 
    IntListParser, 
    TupleParser, 
    BoolParser, 
    SortTransform, 
    SetParser,
)

from aocd.models import default_user, Puzzle, User
from aocd.get import current_day, most_recent_year
from aocd import get_data

sample_input_file = os.path.basename(__file__).split('.')[0] + 'sampleinput.txt'
input_file = os.path.basename(__file__).split('.')[0] + 'input.txt'

def create_input_files():
    # sample_input_file = os.path.basename(__file__).split('.')[0] + 'sampleinput.txt'
    # input_file = os.path.basename(__file__).split('.')[0] + 'input.txt'

    with open(sample_input_file, 'w') as file: pass
    with open(input_file, 'w') as file: pass

def clipboard_input_file_names():
    print('code .\\' + sample_input_file, end='; ')
    print('code .\\' + input_file)

    pyperclip.copy('code .\\' + sample_input_file + '; code .\\' + input_file)

def get_current_session_id():
    url = 'https://adventofcode.com'

    session = requests.Session()
    session.get(url)

    for key in session.cookies.keys():
        print(key)
    # return session.cookies['sessionid']



def get_raw_data(session=None, day=None, year=None) -> str:
    if session is None:
        user = default_user()
    else:
        user = User(token=session)

    if day == None: current_day()
    if year == None: most_recent_year()

    return Puzzle(year=year, day=day, user=user).input_data


# create_input_files()
# clipboard_input_file_names()

# session = '53616c7465645f5f354dcc0184fa6606642fb5e4c4c6538183b78954f110f1a53a6e453ac1ccad83afee64d0ccd865b7cbb0f2fe6e420546bc188ed087265ed9'

print(get_data(day=1, year=2024))


# os.remove(sample_input_file)
# os.remove(input_file)