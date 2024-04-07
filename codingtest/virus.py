import sys
from collections import deque
input = sys.stdin.readline
# direaction = [(1,0),(-1,0),(0,-1),(0,1)]

def bfs(start):
    queue = deque([start])
    count = 0
    visit[1] = True
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visit[i] == False:
                queue.append(i)
                visit[i] = True
                count+=1
    return count
n = int(input())
m = int(input())
graph=[[] for _ in range(n+1)]
visit=[False] * (n+1)
for i in range(m):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

result = bfs(1) 
print(result)       