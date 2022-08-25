https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    get=int(len(nums)/2)
    nums=sorted(nums)
    cnt=[]
    answer = 0

    for i in range(len(nums)):
        if nums[i] in cnt:
            continue
        else:
            cnt.append(nums[i])
    if get<len(cnt):
        answer=len(cnt)-(len(cnt)-get)
    elif get>len(cnt):
        answer=get-(get-len(cnt))
    else:
        answer=len(cnt)
    return answer
