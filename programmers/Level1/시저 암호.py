#소문자 97-122
#대문자 65-90
def solution(s,n):
    arr=list(s)
    result=[]
    for i in arr:
        #소문자
        #1
        if i.islower():
            if ord(i)+n>122:
                i=chr(ord(i)+n-26)
            else:
                i=chr(ord(i)+n)
            result.append(i)
        elif i.isupper():
            if ord(i)+n>90:
                i=chr(ord(i)+n-26)
            else:
                i=chr(ord(i)+n)
            result.append(i)
        else:
            result.append(' ')
    result="".join(result)
    return result
print(solution('bC',25))
#오답노트
#1
'''
if i.isupper():
    i=chr((ord(i)-ord('A')+n)%26+ord('A'))
elif i.islower():
    i=chr((ord(i)-ord('a')+n)%26+ord('a'))
'''