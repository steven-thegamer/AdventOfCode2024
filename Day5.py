rules_front = {}
rules_back = {}
with open('Untitled2.txt') as f:
    lines = f.readlines()
    for line in lines:
        key_value = line.split('|')
        front_value = key_value[0]
        back_value = key_value[1][0:-1]
        if front_value in rules_front:
            rules_front[front_value].append(back_value)
        else:
            rules_front[front_value] = [back_value]
        if back_value in rules_back:
            rules_back[back_value].append(front_value)
        else:
            rules_back[back_value] = [front_value]

total = 0
all_incorrect_rows = []

# Task 1

with open('Untitled3.txt') as g:
    lines = g.readlines()
    for line in lines:
        whole_line = line[0:-1]
        arr_line = whole_line.split(',')
        n = len(arr_line)
        good_row = True
        for i in range(n):
            for j in range(n):
                if i < j:
                    if arr_line[i] in rules_front and arr_line[j] not in rules_front[arr_line[i]]:
                        good_row = False
                        all_incorrect_rows.append(arr_line)
                        break
                elif i > j:
                    if arr_line[i] in rules_back and arr_line[j] not in rules_back[arr_line[i]]:
                        good_row = False
                        all_incorrect_rows.append(arr_line)
                        break
            if good_row == False:
                break
        if good_row:
            total += int(arr_line[n//2])
print(total)

# Task 2

total = 0

for line in all_incorrect_rows:
    n = len(line)
    i = 0
    checker = True
    while checker:
        checker = False
        for i in range(n):
            for j in range(n):
                if i < j:
                    if line[j] in rules_front and line[i] in rules_front[line[j]]:
                        line[i],line[j] = line[j],line[i]
                        checker = True
                elif j < i:
                    if line[j] in rules_back and line[i] in rules_back[line[j]]:
                        line[i],line[j] = line[j],line[i]
                        checker = True
    total += int(line[n//2])

print(total)
