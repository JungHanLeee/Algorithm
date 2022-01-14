def solution(s):
    num1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    str1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    check_list = []
    total = []
    result = []
    for i in range(len(s)):
        if s[i] not in num1:
            check_list.append(s[i])
            result = "".join(check_list)
        else:
            total.append(s[i])
        if result in str1:
            total.append(num1[str1.index(result)])
            check_list = []
            result = []

    answer = "".join(total)
    answer=int(answer)
    return answer