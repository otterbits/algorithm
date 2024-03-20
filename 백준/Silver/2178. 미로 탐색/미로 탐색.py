from collections import deque
import sys

# n x m 미로 크기
n, m = map(int, sys.stdin.readline().rstrip().split())
# n 횟수만큼 maze를 받아서 list로 저장
maze = [sys.stdin.readline().rstrip() for _ in range(n)]
# 방문했는지 여부를 False로 저장
visited = [[False] * m for _ in range(n)]

# x좌표, y좌표를 줘 상하좌우를 표현
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# [현재 x좌표, 현재 y좌표, 칸 수]
location = deque([[0, 0, 1]])
# 맨 처음 좌표는 방문했다고 표시
visited[0][0] = True

while location:
		# bfs는 queue의 특성인 선입선출을 이용함.
    x, y, dist = location.popleft()
		
		# 먼저 도착한 경우에서 칸 수를 출력
    if x == n - 1 and y == m - 1:
        print(dist)
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
				
				# 움직인 좌표가 미로 안에 있고, 그 좌표가 막혀있지 않고, 방문하지 않았다면,
        if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == '1' and not visited[nx][ny]:
            # 움직인 좌표를 방문하고, 현재 좌표에 칸 수를 한 칸 더하여 추가해준다.
            visited[nx][ny] = True
            location.append([nx, ny, dist + 1])