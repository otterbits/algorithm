import sys
from collections import deque

n, k = map(int, (sys.stdin.readline().split()))

human = deque()
result = []

for i in range(1, n+1):
    human.append(i)

while human:
    for _ in range(k-1):
        human.append(human.popleft())
    result.append(human.popleft())

print(str(result).replace('[', '<',).replace(']', '>'))