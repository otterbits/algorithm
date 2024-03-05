import sys

brackets = sys.stdin.readline().rstrip()
stack = []
answer = 0

for i in range(len(brackets)):
    # 레이저가 아닐 때, stack에 "(" 열린 괄호를 추가한다.
    if brackets[i] == "(" and brackets[i+1] != ")":
        stack.append("(")
    # () 레이저가 나왔을 때, 그전에 stack에 있는 "(" 열린 괄호 수 만큼 선이 추가된다.
    if brackets[i] == ")":
        if brackets[i-1] == "(":
            answer += len(stack)
    # 레이저가 아닌데 ")" 닫힌 괄호가 나왔다면, 선 마무리라는 뜻이므로 stack의 "(" 열린 괄호 하나를 빼고, 선 개수를 하나 추가한다.
        else:
            stack.pop()
            answer += 1

print(answer)