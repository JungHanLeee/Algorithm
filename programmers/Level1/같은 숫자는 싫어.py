def solution(arr):
    answer=[]
    answer.append(arr[0])
    arr=arr[1:]
    for i in arr:
        if answer[-1]==i:
            continue
        else:
            answer.append(i)
    return answer