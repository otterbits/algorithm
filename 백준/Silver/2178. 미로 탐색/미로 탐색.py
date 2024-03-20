from collections import deque
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
maze = [sys.stdin.readline().rstrip() for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

location = deque([[0, 0, 1]])

while location:
    x, y, dist = location.popleft()

    if x == n - 1 and y == m - 1:
        print(dist)
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == '1' and not visited[nx][ny]:
            visited[nx][ny] = True
            location.append([nx, ny, dist + 1])