https://school.programmers.co.kr/learn/courses/30/lessons/12928
  
def solution(n):
    result=[]
    for i in range(1,n+1):
        if n%i==0:
            result.append(i)

    return sum(result)
