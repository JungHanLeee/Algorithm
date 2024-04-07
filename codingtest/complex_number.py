import sys
from collections import deque

def bfs(matrix,x,y):
    count = 0  
    queue = deque([(x,y)])
    directions = [(1,0),(-1,0),(0,-1),(0,1)]
  
    while queue:
        x, y = queue.popleft()
        for dr,dy in directions:
            nx,ny = x+dr, y+dy
            if 0<=nx<len(matrix) and 0<=ny<len(matrix[0]) and matrix[nx][ny] == 1:
                queue.append((nx,ny))
                matrix[nx][ny]=0
                count+=1
    return count

n = int(input())
matrix = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

result = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            s = bfs(matrix,i,j)
            result.append(s)

print(len(result))
result.sort()
for i in result:
    print(i)
  