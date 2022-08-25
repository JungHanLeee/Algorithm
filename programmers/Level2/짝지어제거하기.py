https://school.programmers.co.kr/learn/courses/30/lessons/12973
  
def solution(s):
    answer = 0
    arr=list(s)
    stack=[]
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in range(len(arr)):
        stack.append(arr[i])
        if len(stack)>1:
            if stack[-1]==stack[-2]:
                stack.pop()
                stack.pop()
    if len(stack)>=1:
        answer=0
    else:
        answer=1    
    
    return answer
