def solution(s):
    if len(s)%2!=0:
        answer=s[len(s)//2]
    else:
        #1
        arr1 = s[:len(s) // 2]
        arr2 = s[len(s) // 2:]
        answer = arr1[-1] + arr2[0]
    return answer

#오답노트
#1 따로 arr1,arr2변수를 생성안하고 바로 슬라이싱처리 가능
# answer = (s[len(s) // 2 - 1:len(s) // 2 + 1])
