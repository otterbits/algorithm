from collections import deque
import sys
input = sys.stdin.readline

com = int(input())
connect = int(input())
# 1부터 시작
network = [[] for _ in range(com + 1)]
visited = [False] * (com + 1)
cnt = 0

for _ in range(connect):
    first, last = map(int, input().split())
    network[first].append(last)
    network[last].append(first)

queue = deque([1])
while queue:
    current = queue.popleft()
    visited[1] = True
    for i in network[current]:
        if not visited[i]:
            queue.append(i)
            visited[i] = True
            cnt += 1

print(cnt)


