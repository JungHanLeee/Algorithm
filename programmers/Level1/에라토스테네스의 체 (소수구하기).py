import math

def solution(n):
    # 모두 소수로 간주
    arr=[True for i in range(n)]
    cnt=0
    # n의 제일 작은 배수들 중에서 제일 큰 수=sqrt(n)
    for i in range(2,int(math.sqrt(n))+1):
        #i가 소수인 경우
        if arr[i]==True:
            for j in range(i+i,n,i): #i이후 i의 배수들을 False처리
                arr[j]=False
    #소수 목록 산출
    for i in range(2,len(arr)):
        if arr[i]==True:
            cnt+=1

    return cnt
print(solution(10))