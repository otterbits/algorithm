import sys
input = sys.stdin.readline

N, M = map(int, input().split())
height = list(map(int, input().split()))

start = 1
end = max(height)

result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in height:
        # 잘랐을 때 나무 높이 총합 계산
        if i > mid:
            total += i - mid
    # 나무의 높이가 최솟값보다 높을 경우 높이 저장, 더 자르기 (오른쪽 부분 탐색)
    if total >= M:
        result = mid
        start = mid + 1
    # 나무의 높이가 최솟값보다 낮을 경우, 덜 자르기 (왼쪽 부분 탐색)
    else:
        end = mid - 1

print(result)