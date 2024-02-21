import sys

answer = list(sys.stdin.readline().rstrip())
cursor = []
count = int(sys.stdin.readline().rstrip())
for _ in range(count):
    command = sys.stdin.readline().rstrip()
    if command == 'L' and answer:
        cursor.append(answer.pop())
    elif command == 'D' and cursor:
        answer.append(cursor.pop())
    elif command == 'B' and answer:
        answer.pop()
    elif 'P' in command:
        answer.append(command.lstrip('P '))

while cursor:
    answer.append(cursor.pop())
for i in answer:
    print(i, end='')