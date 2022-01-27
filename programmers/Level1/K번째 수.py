def solution(array, commands):
    result = []
    for i in range(len(commands)):
        arr = array[commands[i][0] - 1:commands[i][1]]
        arr = sorted(arr)
        result.append(arr[commands[i][2] - 1])
    return result