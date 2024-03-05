import sys

N = int(sys.stdin.readline().rstrip())
sequence = list(map(int, sys.stdin.readline().split()))
# index를 담을 stack
stack_index = []
# 수만큼 -1 list
answer = [-1] * N

for i in range(N):
    # 비교할 index가 있을 시, 현재 index 전의 값과 현재 index의 값 비교
    while stack_index and sequence[stack_index[-1]] < sequence[i]:
        # 현재 index 전이 적다면 answer[현재 index 전]은 현재 index의 값이다.
        answer[stack_index[-1]] = sequence[i]
        # 현재 index 전은 비교했으니 전전과 비교하도록 pop
        stack_index.pop()
    # 현재 index 전이 크다면 stack에 기록
    stack_index.append(i)
    
print(*answer)