print('')
print("This will print Pascal's triangle with modular arithmetic")
n = int(input('Number of iterations: '))
m = int(input('Modulus: '))
fyn = input('Filter? y/n: ')

if fyn == 'y':
    f = int(input('Number to display:'))

linelist = []

def makeline(vertic):
    line = ''
    if vertic == 0:
        line = '1'
    else:
        line = '1'
        for a in range(1,vertic):
            line = line + str((int(linelist[vertic-1][a-1]) + int(linelist[vertic-1][a])) % m)
        line = line + '1'
    return line

def insertspaces(line):
    newline =  '1'
    for a in range(len(line)-1):
        newline =  newline + ' ' + line[a+1]
    return newline

def filter_line(line,f):
    newline = ''
    for ch in line:
        if ch == str(f) or ch == ' ':
            newline = newline + ch
        else:
            newline = newline + '-'
    return newline


if fyn == 'y':
    for a in range(n):
        linelist.append(makeline(a))
    for b in range(0,len(linelist)):
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

