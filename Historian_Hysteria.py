
# Online Python - IDE, Editor, Compiler, Interpreter
a = input()
arr = a.split()
left = []
right = []
i = 0
while i < len(arr):
    left.append(int(arr[i]))
    right.append(int(arr[i+1]))
    i += 2
sorted_left = sorted(left)
sorted_right = sorted(right)

# Part 1
distance = 0
for j in range(len(left)):
    distance += abs(sorted_left[j] - sorted_right[j])
print(distance)

# Part 2
similarity_score = 0
dict_value = {}
for j in range(len(right)):
    value = sorted_right[j]
    if value in dict_value:
        dict_value[value] += 1
    else:
        dict_value[value] = 1
for j in range(len(left)):
    value = sorted_left[j]
    if value in dict_value:
        similarity_score += value * dict_value[value]
print(similarity_score)
