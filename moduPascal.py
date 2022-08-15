from os import get_terminal_size

line_list = []


def make_line(line_number):
    line = '1'
    if line_number != 0:
        for a in range(1, line_number):
            above_int_left = int(line_list[line_number - 1][a - 1])
            above_int_right = int(line_list[line_number - 1][a])
            next_int = (above_int_left + above_int_right) % m
            line += str(next_int)
        line += '1'
    return line


def insert_spaces(line):
    newline = '1'
    for a in range(len(line)-1):
        newline += ' ' + line[a + 1]
    return newline


def filter_line(line, fnum):
    newline = ''
    fchar = str(fnum)
    for ch in line:
        if ch == fchar or ch == ' ':
            newline += ch
        else:
            newline += '-'
    return newline


def userinput_onlyint(inmsg):
    isint = False
    while not isint:
        usrin = input(inmsg)
        isint = True
        for c in usrin:
            if c not in '0123456789':
                isint = False
        if not isint:
            print('Please enter a number character')
    return int(usrin)


# User loop
cont = ''
while cont != 'q':
    # User input
    print('')
    print("This will print Pascal's triangle with modular arithmetic")
    n = userinput_onlyint('Number of iterations (press 0 to adjust to your terminal window size): ')
    if n == 0:  # Adjusts both vertically and horizontally. TODO: add separate horizontal and vertical adjustment
        size = get_terminal_size()
        for a in range(size.lines - 1):
            if size.columns >= a*2 - 1:
                n = a
    m = userinput_onlyint('Modulus: ')
    fyn = input('Filter? y/n: ')
    while fyn not in 'yn':
        print('Sorry, try again')
        fyn = input('Filter? y/n: ')
    if fyn == 'y':
        f = int(input('Number to display:'))
    print('')

    # Triangle loop
    line_list = []
    for a in range(n):
        line_list.append(make_line(a))
        spaces = int(n - a - 1)
        if fyn == 'n':
            print(' ' * spaces + insert_spaces(make_line(a)))
        else:
            print(' ' * spaces + filter_line(insert_spaces(make_line(a)), f))

    print('')
    cont = input('Press q to quit, or any other key to continue ')
