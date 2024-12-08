def generateAllBinaryStrings(n, arr, i, result):
    if i == n:
        result.append(arr[:])
        return
    arr[i] = 0
    generateAllBinaryStrings(n, arr, i + 1, result)
    arr[i] = 1
    generateAllBinaryStrings(n, arr, i + 1, result)
    # Additional for Task 2
    arr[i] = 2
    generateAllBinaryStrings(n, arr, i + 1, result)

def getAllBinaryStrings(n):
    arr = [None] * n
    result = []
    generateAllBinaryStrings(n, arr, 0, result)
    return result

with open('input.txt') as f:
    lines = f.readlines()
    # Task 1
    total = 0
    for line in lines:
        whole_line = line.split(': ')
        result = whole_line[0]
        question = whole_line[1].split()
        n = len(question)
        all_possibilities = getAllBinaryStrings(n)
        for p in all_possibilities:
            answer = 0
            for i in range(n):
                num = int(question[i])
                if p[i] == 0:
                    answer += num
                elif p[i] == 1:
                    answer *= num
                # Additional for Task 2
                elif p[i] == 2:
                    answer = answer * 10 ** len(question[i]) + num
            if int(result) == answer:
                total += answer
                break
    print(total)
            
