import os

# print(os.path.basename(__file__).split('.')[0])

def create_input_files():
    sample_input_file = os.path.basename(__file__).split('.')[0] + 'sampleinput.txt'
    input_file = os.path.basename(__file__).split('.')[0] + 'input.txt'

    with open(sample_input_file, 'w') as file: pass
    with open(input_file, 'w') as file: pass

for i in range(1,10):
    old_file = "day" + str(i) + ".py"
    new_file = 'day0' + str(i) + '.py'

    print(f'old: {old_file}, new: {new_file}')


    os.rename(old_file, new_file)

