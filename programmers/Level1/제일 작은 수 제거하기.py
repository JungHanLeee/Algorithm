def solution(arr):
    answer = []
    arr.remove(min(arr))
    if len(arr)==0:
        answer.append(-1)
        return answer
    return arr
