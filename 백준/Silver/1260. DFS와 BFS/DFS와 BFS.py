import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())

# 1부터 시작하므로
graph = [[] for _ in range(N + 1)]

visited1 = [False]*(N+1)
visited2 = visited1.copy()


for _ in range(M):
    first, end = map(int, input().split())
    graph[first].append(end)
    graph[end].append(first)
    graph[first].sort()
    graph[end].sort()

def dfs(start, graph, visited):
    visited[start] = True
    print(start, end=" ")
    for i in graph[start]:
        if not visited[i]:
            dfs(i, graph, visited)


def bfs(start, graph, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        current = queue.popleft()
        print(current, end=" ")
        for i in graph[current]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True



dfs(V, graph, visited1)
print()

bfs(V, graph, visited2)
