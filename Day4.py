arr = []
with open('Untitled2.txt') as f:
    lines = f.readlines()
    for line in lines:
        arr.append(list(line.strip())) # Just to exclude /n from the array

max_x = len(arr[0])
max_y = len(arr)

# Task 1

xmas = 0

for y in range(max_y):
    for x in range(max_x):
        if arr[y][x] == 'X':
            if y < max_y - 3 and arr[y+1][x] == 'M' and arr[y+2][x] == 'A' and arr[y+3][x] == 'S':
                xmas += 1
            if y >= 3 and arr[y-1][x] == 'M' and arr[y-2][x] == 'A' and arr[y-3][x] == 'S':
                xmas += 1
            if x < max_x - 3 and arr[y][x+1] == 'M' and arr[y][x+2] == 'A' and arr[y][x+3] == 'S':
                xmas += 1
            if x >= 3 and arr[y][x-1] == 'M' and arr[y][x-2] == 'A' and arr[y][x-3] == 'S':
                xmas += 1
            if y < max_y - 3 and x >= 3 and arr[y+1][x-1] == 'M' and arr[y+2][x-2] == 'A' and arr[y+3][x-3] == 'S':
                xmas += 1
            if y < max_y - 3 and x < max_x - 3 and arr[y+1][x+1] == 'M' and arr[y+2][x+2] == 'A' and arr[y+3][x+3] == 'S':
                xmas += 1
            if y >= 3 and x >= 3 and arr[y-1][x-1] == 'M' and arr[y-2][x-2] == 'A' and arr[y-3][x-3] == 'S':
                xmas += 1
            if y >= 3 and x < max_x - 3 and arr[y-1][x+1] == 'M' and arr[y-2][x+2] == 'A' and arr[y-3][x+3] == 'S':
                xmas += 1
            
            
print(xmas)

# Task 2

x_mas = 0
for y in range(max_y):
    for x in range(max_x):
        checker = 0
        if arr[y][x] == 'A' and x >= 1 and y >= 1 and x < max_x - 1 and y < max_y - 1:
            if (arr[y-1][x+1] == 'M' and arr[y+1][x-1] == 'S'):
                checker += 1
            if arr[y-1][x+1] == 'S' and arr[y+1][x-1] == 'M':
                checker += 1
            if (arr[y+1][x+1] == 'S' and arr[y-1][x-1] == 'M'):
                checker += 1
            if arr[y+1][x+1] == 'M' and arr[y-1][x-1] == 'S':
                checker += 1
        if checker == 2:
            x_mas += 1

print(x_mas)
