import numpy as np

with open('input.txt') as f:
    lines = f.readlines()
    counter = 0
    a = [[0,0],
         [0,0]]
    b = []
    total = 0
    for line in lines:
        if line == '\n':
            counter = -1
            a = [[0,0],
                 [0,0]]
            b = []
        elif counter == 2:
            b = line[7:].split(', ')
            # The addition of 10000000000000 is due to task 2
            m = int(b[0][2:]) + 10000000000000
            n = int(b[-1][2:-1]) + 10000000000000
            # Find the deterimnant value
            det = a[0][0] * a[1][1] - a[0][1] * a[1][0]
            if det != 0:
                x = (a[1][1] * m - a[0][1] * n) / det
                y = (a[0][0] * n - a[1][0] * m) / det
                if x.is_integer() and y.is_integer():
                    total += int(x) * 3 + int(y)
        else:
            results = line[10:].split(', ')
            results[-1] = results[-1][:-1]
            a[0][counter] = int(results[0][2:])
            a[1][counter] = int(results[1][2:])
        counter += 1
print(total)
