def solution(a, b):
    thirty_one = [1, 3, 5, 7, 8, 10, 12]
    thirty = [4, 6, 9, 11]
    tweenty_nine = [2]
    arr = []
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    for i in range(1, a + 1):
        if i != a:
            if i in thirty_one:
                arr.append(31 % 7)
            elif i in thirty:
                arr.append(30 % 7)
            else:
                arr.append(29 % 7)
        #마지막 달은 일자까지 계산
        else:
            if i in thirty_one:
                arr.append(b % 7)
            elif i in thirty:
                arr.append(b % 7)
            else:
                arr.append(b % 7)
    result = sum(arr)
    if result > 7:
        result = result % 7

    answer = day[result - 1]

    return answer
print(solution(5,24))