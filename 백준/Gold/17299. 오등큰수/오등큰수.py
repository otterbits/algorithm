import sys

N = int(sys.stdin.readline().rstrip())
sequence = list(map(int, sys.stdin.readline().split()))

# 기본값이 -1
answer = [-1] * N
# 해당 값이면서 index이자 count
count = [0] * 1000001
# 현재 index
index = []

for i in sequence:
    count[i] += 1

for j in range(N):
    # 현재 index의 count와 제일 최근 index의 count 비교
    while index and count[sequence[index[-1]]] < count[sequence[j]]:
        # 최근 index가 작다면 현재 index의 숫자를 정답에 넣어줌
        answer[index[-1]] = sequence[j]
        # 최근 index는 왼쪽으로 한 칸 옮김
        index.pop()
    # 최근 index가 크다면 오른쪽으로 한 칸 옮김
    index.append(j)

print(*answer)

