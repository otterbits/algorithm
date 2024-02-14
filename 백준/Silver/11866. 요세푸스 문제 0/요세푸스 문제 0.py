import sys
from collections import deque

n, k = map(int,(sys.stdin.readline().split()))
table = deque()
result = []
for i in range(1, n+1):
    table.append(i)
while table:
    for i in range(k-1):
        table.append(table.popleft())
    result.append(table.popleft())

print("<", ', '.join(map(str, result)), ">", sep="")