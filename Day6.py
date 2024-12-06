
# Online Python - IDE, Editor, Compiler, Interpreter
walls = []
curr_pos = [0,0]
direction = 0 # 0 is up, 1 is right, 2 is down, 3 is left
with open('Untitled2.txt') as f:
    lines = f.readlines()
    max_y = len(lines)
    max_x = len(lines[0]) - 1
    for y in range(max_y):
        for x in range(max_x):
            if lines[y][x] == '#':
                walls.append([x,y])
            elif lines[y][x] == '^':
                curr_pos = [x,y]
                
# Task 1
visited_pos = {tuple(curr_pos):1}
while True:
    if direction == 0: # goes up
        curr_pos[1] -= 1
    elif direction == 1: # goes right
        curr_pos[0] += 1
    elif direction == 2: # goes down
        curr_pos[1] += 1
    elif direction == 3: # goes left
        curr_pos[0] -= 1
    if curr_pos in walls:
        if direction == 0:
            curr_pos[1] -= -1
        elif direction == 1:
            curr_pos[0] += -1
        elif direction == 2:
            curr_pos[1] += -1
        elif direction == 3:
            curr_pos[0] -= -1
        direction += 1
        direction = direction % 4
    check = curr_pos[0] >= 0 and curr_pos[1] >= 0 and curr_pos[0] < max_x and curr_pos[1] < max_y
    if check == False:
        break
    visited_pos[tuple(curr_pos)] = 1

print(len(visited_pos))

# Task 2


