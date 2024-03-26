import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for i in range(N)]
# 끝나는 시각 기준 오름차순 정렬 (일찍 끝나야 다음 회의를 더 많이 진행할 수 있음)
graph.sort(key=lambda x: (x[1], x[0]))
std = 0
cnt = 0

for start, end in graph:
    # 지금 종료 시간보다 다음 시작 시간이 클 경우
    if start >= std:
        cnt += 1
        # 지금 종료 시간을 다음 종료 시간으로 변경
        std = end

print(cnt)
