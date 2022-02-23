#4,[1,2,2,2]
def solution(N,stages):
    fail=[]
    for i in range(1,N+1):
        people=0
        for j in range(len(stages)):
            if i<=stages[j]:
                people+=1
        if max(stages)<i:
            fail.append(0.0)
        else:
            fail.append(stages.count(i)/people)
        print(fail)
    print(fail)
    temp=sorted(fail,reverse=True)
    result=[]
    for i in range(N):
        for j in range(N):
            if temp[i]==fail[j]:
                result.append(j+1)
                fail[j]=1000
                continue
    return result
print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
