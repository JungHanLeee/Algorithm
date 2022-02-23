def solution(a,b):
    if a<b:
        result=[i for i in range(a,b+1,)]
    else:
        result=[i for i in range(b,a+1)]
    return sum(result)
print(solution(1,1))
