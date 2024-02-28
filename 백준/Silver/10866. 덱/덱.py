import sys

cnt = int(sys.stdin.readline())

result = []

for _ in range(cnt):
    command = sys.stdin.readline().rstrip()
    if "push_front" in command:
        result.insert(0, command.strip("push_front "))
    if "push_back" in command:
        result.append(command.strip("push_back "))
    if command == "pop_front":
        if result:
            print(result.pop(0))
        else:
            print(-1)
    if command == "pop_back":
        if result:
            print(result.pop())
        else:
            print(-1)
    if command == "size":
        print(len(result))
    if command == "empty":
        if result:
            print(0)
        else:
            print(1)
    if command == "front":
        if result:
            print(result[0])
        else:
            print(-1)
    if command == "back":
        if result:
            print(result[len(result)-1])
        else:
            print(-1)
