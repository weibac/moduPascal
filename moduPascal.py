linelist = []

def makeline(line_number):
    line = '1'
    if line_number != 0:
        for a in range(1,line_number):
            line += str((int(linelist[line_number-1][a-1]) + int(linelist[line_number-1][a])) % m)
        line += '1'
    return line

def insertspaces(line):
    newline =  '1'
    for a in range(len(line)-1):
        newline += ' ' + line[a+1]
    return newline

def filter_line(line,fnum):
    newline = ''
    fchar = str(fnum)
    for ch in line:
        if ch == fchar or ch == ' ':
            newline += ch
        else:
            newline += '-'
    return newline

#User loop
cont = ''
while cont != 'q':
    #User input
    print('')
    print("This will print Pascal's triangle with modular arithmetic")
    n = int(input('Number of iterations: '))
    m = int(input('Modulus: '))
    fyn = input('Filter? y/n: ')
    while fyn not in 'yn':
        print('Sorry, try again')
        fyn = input('Filter? y/n: ')
    if fyn == 'y':
        f = int(input('Number to display:'))
    print('')

    #Triangle loop
    linelist = []
    for a in range(n):
        linelist.append(makeline(a))
        spaces = int(n - a - 1)
        if fyn == 'n':
            print(' ' * spaces + insertspaces(makeline(a)))
        else:
            print(' ' * spaces + filter_line(insertspaces(makeline(a)),f))
    
    print('')
    cont = input('Press q to quit, or any other key to continue ')

