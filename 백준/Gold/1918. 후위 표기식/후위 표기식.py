import sys

# 출력값 받기
form = list(sys.stdin.readline().strip())
# 정답을 받을 빈 문자열
answer = ''
stack = []

for i in form:
    # 알파벳은 정답에 바로 추가
    if "A" <= i <= "Z":
        answer += i
    else:
        # 스택이 열린 괄호면 추가
        if i == "(":
            stack.append(i)
        else:
            if i == '+' or i == "-":
                # +,-는 우선순위가 제일 낮으므로 스택이 없고 스택 마지막이 열린 괄호일 때까지 스택에 있는 연산자들을 정답에 추가
                while stack and stack[-1] != "(":
                    answer += stack.pop()
                # 마지막에 자기 자신을 스택에 추가
                stack.append(i)
            if i == "*" or i == "/":
                # 스택이 없고 *, -는 스택 마지막이 자기 자신과 같을 경우일 때까지 스택에 있는 연산자들을 정답에 추가
                while stack and (stack[-1] == "*" or stack[-1] == "/"):
                    answer += stack.pop()
                # 마지막에 자기 자신을 스택에 추가
                stack.append(i)
            if i == ")":
                # 스택 끝 연산자가 열린 괄호일 때까지 스택에 있는 연산자들을 정답에 추가
                while stack and stack[-1] != "(":
                    answer += stack.pop()
                # 열린 괄호 빼기
                stack.pop()

# 남아 있는 연산자들 뽑아내기
for i in range(len(stack)):
    answer += stack.pop()

# 열린 괄호 제외
print(answer)