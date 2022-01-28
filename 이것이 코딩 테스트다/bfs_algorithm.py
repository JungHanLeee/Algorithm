from collections import deque

def bfs(graph,start,visited):
    #queue 구현을 위해 deque라이브러리 사용
    queue=dqueue([start])
    #현재 노드를 방문 처리
    visited[start]=True
    #큐가 빌 때까지 반복
    while queue:
        v=queue.popleft()
        print(v,end=' ')
        #아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
graph=[
    [],
    [2,3,8],
    [1,7],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited=[False]*9
bfs(graph,1,visited)
