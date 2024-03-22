import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# def dfs(graph, v, visited):
#     visited[v] = True
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)
#
#
# n, m = map(int, input().split())
# graph = [[] for _ in range(n + 1)]
#
# for _ in range(m):
#     u, v = map(int, input().split())
#     graph[u].append(v)
#     graph[v].append(u)
#
# visited = [False] * (n + 1)
# count = 0
#
# for i in range(1, n + 1):
#     if not visited[i]:
#         dfs(graph, i, visited)
#         count += 1
#
# print(count)
#


def bfs(graph, start, visited):
    visited[start] = True
    queue = deque([start])

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)
count = 0

for i in range(1, n+1):
    if not visited[i]:
        bfs(graph, i, visited)
        count += 1
        
print(count)