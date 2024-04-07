import sys
from collections import deque

n = int(input())
matrix=[]
maxN = 0
# matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))
    for j in range(n):
        if matrix[i][j] > maxN:
            maxN = matrix[i][j]

# print(matrix)

directions=[(1,0),(-1,0),(0,-1),(0,1)]
def bfs(j,k,i,visit):
    queue = deque([(j,k)])
    visit[j][k]=1

    while queue:
        x,y = queue.popleft()

        for dx,dy in directions:
            nx,ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n and matrix[nx][ny] > i and visit[nx][ny] == 0:
                visit[nx][ny]=1
                queue.append((nx,ny))

result=0
for i in range(maxN):
    visit = [[0]*n for _ in range(n)]
    cnt=0
    for j in range(n):
        for k in range(n):
            if matrix[j][k] > i and visit[j][k] == 0:
                bfs(j,k,i,visit)
                cnt+=1
    if result < cnt:
        result = cnt
print(result)