import sys
input = sys.stdin.readline

com = int(input())
connect = int(input())
# 1부터 시작
network = [[] for _ in range(com + 1)]
visited = [False] * (com + 1)

for _ in range(connect):
    first, last = map(int, input().split())
    network[first].append(last)
    network[last].append(first)

cnt = 0
# 무조건 1번 컴퓨터부터 시작이니까
visited[1] = True

# dfs
stack = [1]

while stack:
    current = stack.pop()
    for i in network[current]:
        if not visited[i]:
            visited[i] = True
            stack.append(i)
            cnt += 1

print(cnt)