def solution(s):
    s=list(s)
    print(s)
    false=False
    true=True
    num=['0','1','2','3','4','5','6','7','8','9']
    if len(s)==4 or len(s)==6:
        for i in s:
            if i not in num:
                return false
        return true
    else:
        return false
print(solution("1234"))