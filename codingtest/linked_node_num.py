from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int, input().split())

def bfs(graph, start, visit):
    queue = deque([start])
    visit[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visit[i]:
                queue.append(i)
                visit[i] = True

graph=[[]for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count=0
visit = [False]*(n+1)
for i in range(1,n+1):
    if not visit[i]:
        bfs(graph, i, visit)
        count+=1 

print(count)