import sys
input = sys.stdin.readline

n = int(input())

arr = [list(map(int, reversed(input().rstrip()))) for _ in range(n)]

# print(arr)
# reverse_arr =
result = []
status = False

for i in range(1,len(arr[0])+1):
    result = []
    for j in range(n):
        # print(arr[j][:i])
        if arr[j][:i] in result:
            break
        else:
            result.append(arr[j][:i])
    if len(result) == n:
        print(i)
        break