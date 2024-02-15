import sys

answer = []

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    bracket = sys.stdin.readline().rstrip()
    boolean = True
    stack = []
    for i in bracket:
        if i == "(":
            stack.append("(")
        else:
            if stack:
                stack.pop()
            else:
                boolean = False
                break
    if not stack and boolean:
        print("YES")
    else:
        print("NO")