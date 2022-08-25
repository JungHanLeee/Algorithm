https://school.programmers.co.kr/learn/courses/30/lessons/12951
  
def solution(s):
    s= s.lower()
    s=list(s)

    for i in range(len(s)):
        if i==0:
            if s[i].isdigit():
                continue
            else:
                s[i]=s[i].upper()
        if i>0:
            if s[i-1] ==" ":
                if  s[i].isalpha():
                    s[i]=s[i].upper()
                elif s[i]==" ":
                    continue
            elif s[i].isdigit():
                continue
                
    print(s)
    result = ''.join(s)
    return result
#1 소문자로 변환
#2 list로 바꿔줌
#3 앞 문자가 공백이면 대문자로 변환 
#4 앞 문자가 숫자나 문자면 continue

