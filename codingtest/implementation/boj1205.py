import sys
from collections import deque
input = sys.stdin.readline

rank = 1
n, new_score, p = map(int, input().split())
if n != 0:
    arr = list(map(int, input().split()))
else:
    print(rank)
    quit()
queue = deque(arr)
# print(queue)

for i in range(len(arr)):
    if len(arr) == p and min(arr)>=new_score:
        print(-1)
        quit()
    j = queue.popleft()
    if new_score < j:
        rank+=1

print(rank)
