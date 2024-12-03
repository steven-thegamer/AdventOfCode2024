
# Online Python - IDE, Editor, Compiler, Interpreter
safe = 0
input = []
with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        line_int = [int(x) for x in line.split()]
        input.append(line_int)
unsafes = []

# Task 1

def check_safe_or_not(row):
    i = 1
    n = len(row)
    up = False
    if row[i] < row[i-1]:
        up = False
    elif row[i] > row[i-1]:
        up = True
    else:
        return False
    while i < n:
        if up == True and (row[i] <= row[i-1] or row[i] - row[i-1] > 3):
            return False
        elif up == False and (row[i] >= row[i-1] or row[i-1] - row[i] > 3):
            return False
        i += 1
    return True

for row in input:
    still_safe = check_safe_or_not(row)
    if still_safe == True:
        safe += 1
    # Additional statements for solving Task 2
    else:
        unsafes.append(row)
print(safe)

# Task 2

for row in unsafes:
    n = len(row)
    i = 0
    can_be_safe = False
    while i < n and can_be_safe == False:
        can_be_safe = check_safe_or_not(row[0:i] + row[i+1:n])
        i += 1
    if can_be_safe:
        safe += 1
print(safe)
