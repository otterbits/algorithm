import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for i in range(N)]
# 끝나는 시각 기준 오름차순 정렬
graph.sort(key=lambda x: (x[1], x[0]))
std = 0
cnt = 0

for start, end in graph:
    # 지금 시간보다 시작 시간이 클 경우
    if start >= std:
        cnt += 1
        # 기준점을 끝나는 시간으로 변경
        std = end

print(cnt)
