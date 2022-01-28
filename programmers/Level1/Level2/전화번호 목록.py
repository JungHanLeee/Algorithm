phone_book=["119", "97674223", "1195524421"]
def solution(phone_book):
    pb=sorted(phone_book)
    for i in range(1,len(pb)):
        tmp=len(pb[i-1])
        print(pb[i-1][0:tmp],pb[i][0:tmp])
        if pb[i-1][0:tmp]==pb[i][0:tmp]:
            return False
    return True
print(solution(phone_book))

#다른 사람풀이
#zip,startswith이용 (endswith도 있음)
def solution(phoneBook):
    phoneBook = sorted(phoneBook)
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

#hash이용
#잘이해안됨
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer