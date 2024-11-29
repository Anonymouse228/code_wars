# https://www.codewars.com/kata/5839c48f0cf94640a20001d3


def land_perimeter(arr):  # the first solution
    arr = ['OO' + 'O' * len(arr[0])] + arr + ['O' * len(arr[0])]
    count = 0

    for i in range(len(arr) - 1):
        arr[i+1] = 'O' + arr[i+1] + 'O'

        for j in range(1, len(arr[i]) - 1):
            if arr[i][j] == 'X':
                for i1, j1 in (-1, 0), (1, 0), (0, -1), (0, 1):
                    count += 1 if arr[i+i1][j+j1] == 'O' else 0

    return f'Total land perimeter: {count}'  # perimeter of all the islands


def land_perimeter_2(arr):  # The neatest solution
    I, J = len(arr), len(arr[0])
    count = 0

    for i in range(I):
        for j in range(J):
            if arr[i][j] == 'X':
                if j == 0     or arr[i][j-1] == 'O': count += 1
                if j == J - 1 or arr[i][j+1] == 'O': count += 1
                if i == 0     or arr[i-1][j] == 'O': count += 1
                if i == I - 1 or arr[i+1][j] == 'O': count += 1

    return f'Total land perimeter: {count}'  # perimeter of all the islands

a = ['XOOO',
     'XOXO',
     'XOXO',
     'OOXX',
     'OOOO']

print(land_perimeter_2(a))
