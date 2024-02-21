import sys

answer = []
stack = []
start = 1
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    end = int(sys.stdin.readline().rstrip())
    while start <= end:
        stack.append(start)
        answer.append('+')
        start += 1

    if end == stack[-1]:
        stack.pop()
        answer.append('-')

    else:
        print('NO')
        break
else:
    print('\n'.join(answer))