import sys
from collections import deque

def bfs(array, visit):
  count = 0
  for i in range(len(array)):
    if visit[i]==0:
      queue = deque([(i)])
      visit[0] = 1
      while queue:
        x = queue.popleft()
        nx = array[x]-1
        if visit[nx] == 0:  # 인덱스 범위 체크 추가
            visit[nx] = 1
            queue.append(nx)  # 튜플 형태로 전달
      count += 1
  return count

c = int(input())
result = []
for _ in range(c):
  n = int(input())
  array = list(map(int, sys.stdin.readline().split(' ')))
  visit = [0 for _ in range(n)]
  result = bfs(array,visit)
  print(result)
