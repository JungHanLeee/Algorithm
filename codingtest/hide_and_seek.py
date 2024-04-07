from collections import deque
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def bfs(n):
    # visit[n]=True
    queue = deque([n])

    while queue:
        x = queue.popleft()
        if x == k:
            return visit[x]
        for i in (x-1,x+1,2*x):
            if 0<= i < 100001 and not visit[i]:
                visit[i] = visit[x]+1
                queue.append(i) 
n, k = map(int, input().split())
visit=[0]*100001
print(bfs(n))
