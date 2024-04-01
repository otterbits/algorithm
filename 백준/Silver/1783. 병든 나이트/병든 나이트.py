import sys
input = sys.stdin.readline

# 세로, 가로
N, M = map(int, input().split())

result = 1

if N == 1:
    result = 1
elif N == 2:
    result = min(4, (M + 1) // 2)
elif M <= 6:
    result = min(4, M)
else:
    result = M - 2

print(result)
