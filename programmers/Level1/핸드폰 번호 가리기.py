#리스트로 바꾼 후 슬라이싱을 이용해 뒤에 숫자만 남기고 앞은 *로 치환
def solution(phone_number):
    phone_number=list(phone_number)
    arr1=phone_number[:-4]
    for i in range(len(arr1)):
        arr1[i]='*'
    answer = "".join(arr1+phone_number[-4:])
    return answer