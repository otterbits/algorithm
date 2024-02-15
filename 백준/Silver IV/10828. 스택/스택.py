import sys
n = int(sys.stdin.readline().rstrip())
stack = []

for i in range(n):
    order = sys.stdin.readline().rstrip()
    if "push" in order:
        order, many = order.split(' ')
        stack.append(many)
    elif order == "pop":
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
    elif order == "size":
        print(len(stack))
    elif order == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif order == "top":
        if len(stack) != 0:
            print(stack[len(stack)-1])
        else:
            print(-1)
