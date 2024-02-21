import sys
from collections import deque

cnt = int(sys.stdin.readline().rstrip())
queue = deque()

for _ in range(cnt):
    command = sys.stdin.readline().rstrip()
    if "push" in command:
        num = command.lstrip("push ")
        queue.append(num)
    elif command == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif command == "size":
        print(len(queue))
    elif command == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif command == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command == "back":
        if queue:
            print(queue[len(queue)-1])
        else:
            print(-1)


