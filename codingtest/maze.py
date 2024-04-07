import sys
from collections import deque
n,m = map(int, input().split(' '))

maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
maze[0][0] = 0
result = []
queue = deque([(0,0,1)])

while queue:
  x,y,count = queue.popleft()
  if x == n-1 and y == m-1:
    result.append(count)  
  for dr, dc in directions:
    nr,nc = x + dr, y + dc
    if 0<= nr < n and 0<= nc < m and maze[nr][nc]==1:
      queue.append((nr, nc, count+1))
      maze[nr][nc] = 0
print(min(result))

#print(maze)