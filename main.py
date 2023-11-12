# ANSI color codes
BLACK = '\u001b[40m'
RED = '\u001b[41m'
GREEN = '\u001b[42m'
YELLOW = '\u001b[43m'
WHITE = '\u001b[47m'
END = '\u001b[0m'

def print_color_pattern(color1, color2):
    for i in range(6):
        if i < 3:
            print(f'{GREEN}{"  " * 6}{color1}{"  " * 8}{END}')
        else:
            print(f'{GREEN}{"  " * 6}{color2}{"  " * 8}{END}')

def print_color_blocks():
    for i in range(9):
        if i < 5:
            print(f'{WHITE}{"  " * (5-i)}{BLACK}{"  " * i}{BLACK}{"  " * (i-1)}{WHITE}{"  " * (4-i)}{END}'
                  f'{WHITE}{"  " * (3-i)}{BLACK}{"  " * (i-1)}{BLACK}{"  " * i}{WHITE}{"  " * (5-i)}{END}')
        else:
            print(f'{WHITE}{"  " * (i-3)}{BLACK}{"  " * (8-i)}{BLACK}{"  " * (7-i)}{WHITE}{"  " * (i-4)}{END}'
                  f'{WHITE}{"  " * (i-5)}{BLACK}{"  " * (7-i)}{BLACK}{"  " * (8-i)}{WHITE}{"  " * (i-3)}{END}')

def create_plot_list():
    plot_list = [[0 for _ in range(11)] for _ in range(10)]
    result = [i + 1 for i in range(10)]

    step = round(abs(result[0] - result[9]) / 9, 2)

    for i in range(10):
        for j in range(11):
            if j == 0:
                plot_list[i][j] = step * (9-i) + step

    for i in range(10):
        for j in range(10):
            if abs(plot_list[i][0] - result[j]) < step:
                plot_list[i][j] = 1

    return plot_list

def print_plot_list(plot_list):
    for i in range(10):
        line = ''
        for j in range(10):
            if j == 0:
                line += f'\t{int(plot_list[i][j])}\t'
            if plot_list[i][j] == 0:
                line += '..'
            if plot_list[i][j+1] == 1:
                line += '//'
        print(line)
    print('\t0\t1 2 3 4 5 6 7 8 9')

def process_sequence_file(file_path='sequence.txt'):
    result_4 = []

    with open(file_path) as file:
        for num_str in file:
            num = float(num_str)
            if 0 <= abs(num) <= 5:
                result_4.append(num)

    return result_4

# 1
print_color_pattern(YELLOW, RED)

# 2
print_color_blocks()

# 3
plot_list = create_plot_list()
print_plot_list(plot_list)

# 4
result_4 = process_sequence_file()
print(result_4)
