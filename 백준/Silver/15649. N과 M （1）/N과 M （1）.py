import sys

input = sys.stdin.readline

N, M = map(int, input().split())
result = []
visited = [False] * (N + 1)


def recur():
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            recur()
            visited[i] = False
            result.pop()


recur()
