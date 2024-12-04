
# Online Python - IDE, Editor, Compiler, Interpreter
whole_string = ''
total = 0
with open('Untitled3.txt') as f:
    lines = f.readlines()
    whole_string = ''.join(lines)

# Task 1

i = 0
index_with_muls = []
while True:
    i = whole_string.find('mul(',i)
    if i == -1:
        break
    index_with_muls.append(i)
    i += 1

for i in index_with_muls:
    j = whole_string.find(')',i)
    if j - i <= 11:
        get_value_in_between = whole_string[i+4:j]
        number_arr = get_value_in_between.split(',')
        if len(number_arr) == 2 and number_arr[0].isdigit() and number_arr[1].isdigit():
            total += int(number_arr[0]) * int(number_arr[1])

print(total)

# Task 2

total = 0

do_index = []
dont_index = []
i = 0
while True:
    i = whole_string.find('do()',i)
    if i == -1:
        break
    do_index.append(i)
    i += 1

i = 0
while True:
    i = whole_string.find("don't()",i)
    if i == -1:
        break
    dont_index.append(i)
    i += 1

do = True
index_dont = -1
if len(dont_index) != 0:
    index_dont = dont_index[0]

index_do = -1
if len(do_index) != 0:
    index_do = do_index[0]

new_index_with_muls = []

for index in index_with_muls:
    if index > index_dont and index_dont != -1:
        if do == True:
            do = False
        dont_index.pop(0)
        if len(dont_index) != 0:
            index_dont = dont_index[0]
        else:
            index_dont = -1
    if index > index_do and index_do != -1:
        if do == False:
            do = True
        do_index.pop(0)
        if len(do_index) != 0:
            index_do = do_index[0]
        else:
            index_do = -1
    if do == True:
        new_index_with_muls.append(index)

for i in new_index_with_muls:
    j = whole_string.find(')',i)
    if j - i <= 11:
        get_value_in_between = whole_string[i+4:j]
        number_arr = get_value_in_between.split(',')
        if len(number_arr) == 2 and number_arr[0].isdigit() and number_arr[1].isdigit():
            total += int(number_arr[0]) * int(number_arr[1])

print(total)
