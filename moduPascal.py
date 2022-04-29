print('')
print("This will print Pascal's triangle with modular arithmetic")
n = int(input('Number of iterations: '))
m = int(input('Modulus: '))
fyn = input('Filter? y/n: ')

if fyn == 'y':
    f = int(input('Number to display:'))
print('')

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


if fyn == 'y':
    for a in range(n):
        linelist.append(makeline(a))
    for b in range(len(linelist)):
        linelist[b] = insertspaces(linelist[b])
        spaces = int(n - b - 1)
        print(' ' * spaces + filter_line(linelist[b],f))
elif fyn == 'n':
    for a in range(n):
        linelist.append(makeline(a))
        spaces = int(n - a - 1)
        print(' ' * spaces + insertspaces(makeline(a)))
else:
    print('Sorry, try again')
