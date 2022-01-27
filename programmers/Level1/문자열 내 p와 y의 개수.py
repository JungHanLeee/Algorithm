def solution(s):
    arr=s.lower
    cnt_p=0
    cnt_y=0
    for i in range(len(arr)):
        if arr[i]=='p':
            cnt_p+=1
        elif arr[i]=='y':
            cnt_y+=1
        else:continue
    if cnt_p==cnt_y:
        return True
    else:
        return False
# 다른사람 풀이
# collections.Counter함수 없이 바로 count함수 이용가능!
def solution(s):
    return s.lower().count('p')==s.lower().count('y')
print(solution("Pyy"))