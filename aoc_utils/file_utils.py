import pyperclip
import os

from aocd.get import current_day, most_recent_year
from aocd import get_data

class Files:
    def __init__(self, day=current_day(), year=most_recent_year()):
        self.day = day
        self.year = year

        day_str = 'day' + str(day).zfill(2)
        # day_str = 'day' + str(day).zfill(2) + 'TEST'

        self.sample_input_file = day_str + 'sampleinput.txt'
        self.input_file = day_str + 'input.txt'

    def update_file_names(self, day, year):
        # day_str = 'day' + str(day).zfill(2)
        day_str = 'day' + str(day).zfill(2) + 'TEST'

        self.sample_input_file = day_str + 'sampleinput.txt'
        self.input_file = day_str + 'input.txt'

f = Files()

def clipboard_input_file_names():
    """
    Clipboards both the main input data and sample input data text files for opening the files quickly via the terminal.
    """
    print('code .\\' + f.sample_input_file, end='; ')
    print('code .\\' + f.input_file)
    pyperclip.copy('code .\\' + f.sample_input_file + '; code .\\' + f.input_file)

def create_input_files(day=current_day(), year=most_recent_year()):
    """
    Creating both the main and sample input text.
    Scrape the main input data into the text file; this requires your Cookie Session ID. (See create_token_file())
    """

    if day != current_day() or year != most_recent_year(): f.update_file_names(day, year)

    if not os.path.exists(f.sample_input_file):
        with open(f.sample_input_file, 'w') as file: pass

    if not os.path.exists(f.input_file):
        with open(f.input_file, 'w') as file:
            file.write(get_data(day=day, year=year))

def get_file_name(type='main'):
    if type == 'main':
        return f.input_file
    elif type == 'sample':
        return f.sample_input_file
    else:
        assert False, "Invalid type. Should only be either 'main' or 'sample'."

def create_token_file(session_id):
    """
    Don't run this function if you haven't 'pip install aocd'; aocd creates the directory ~\\.config\\aocd for the code to work
    Creates a token file for the aocd module to work properly.
    Don't forget to delete this line of code after calling it once to avoid pushing your session-id.
    """

    user_dir = os.path.expanduser('~')
    file_path = user_dir + '\\.config\\aocd\\token'
    file_dir = user_dir + '\\.config\\aocd'

    if not os.path.exists(file_dir):
        assert False, "Directory not found. Use 'pip install aocd' to install the module so that it creates the directory."

    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write(session_id)