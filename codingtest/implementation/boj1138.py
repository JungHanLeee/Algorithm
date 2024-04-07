import sys
input = sys.stdin.readline

n =  int(input())
arr = list(map(int, input().strip().split()))
result = [0]*n

for i in range(n):
    count = 0
    for j in range(n):
        if count == arr[i] and result[j] == 0:
            result[j] = i+1
            break
        elif result[j] == 0:
            count += 1
print(' '.join(map(str, result)))

