https://school.programmers.co.kr/learn/courses/30/lessons/12911
  
def solution(n):
    answer = n
    binaryNum = bin(n)
    arr = list(binaryNum[2:])
    cnt=0
    cnt2=0
    z=1
    for i in (arr):
        if i=='1':
            cnt+=1
    while(True):
        arr2 = list(bin(n+z)[2:])
        for j in (arr2):
            if j=='1':
                cnt2+=1
        if cnt2==cnt:
            answer+=z
            break
        else:
            z+=1
            cnt2=0
    print(arr2)
    return answer
