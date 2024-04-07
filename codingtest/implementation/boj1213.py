import sys
import collections
input = sys.stdin.readline

arr = list(input().rstrip())

# 각 문자의 개수를 세는 딕셔너리 생성
check_word = collections.Counter(arr)

# 팰린드롬을 만들기 위해 사용할 문자열을 저장하는 변수
palindrome = []

# 팰린드롬의 중간에 올 문자를 저장하는 변수
middle_char = ''

# 홀수개인 문자의 개수를 세는 변수
odd_count = 0
result = ''
# 딕셔너리를 순회하면서 팰린드롬을 만들기 위한 문자열을 생성
for k, v in check_word.items():
    if v % 2 == 1:
        odd_count += 1
        middle_char = k
        # 홀수개인 문자의 개수가 2개 이상이면 팰린드롬을 만들 수 없음
        if odd_count >= 2:
            print("I'm Sorry Hansoo")
            exit()

for k,v in sorted(check_word.items()):
    result += (k*(v//2))
print(result + middle_char + result[::-1])
# 팰린드롬의 오른쪽 부분에 중간 문자를 추가하고 뒤집어서 완성
