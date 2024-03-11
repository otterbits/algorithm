import sys

# 출력값 받기
N = int(sys.stdin.readline())
form = list(sys.stdin.readline().strip())
numbers = []

# 후위 표기식을 쌓을 스택
stack = []

for _ in range(N):
    numbers.append(int(sys.stdin.readline().strip()))

for i in form:
    if "A" <= i <= "Z":
        # i가 알파벳이라면, 해당 숫자로 바꿔주기.
        # numbers = [1, 2, 3] form의 알파벳 = [A, B, C] 로 인덱스를 맞춰주는 것
        stack.append(numbers[ord(i)-ord("A")])

    else:
        # 앞의 두 개를 연산해주어야하기 때문에 두 개를 스택에서 꺼낸다.
        num2 = stack.pop()
        num1 = stack.pop()
        if i == "+":
            # 다시 stack에 넣어준다.
            stack.append(num1 + num2)
        if i == "-":
            stack.append(num1 - num2)
        if i == "*":
            stack.append(num1 * num2)
        if i == "/":
            stack.append(num1 / num2)

# f 포매팅으로 둘째 자리수까지 출력
print(f"{stack[0]:.2f}")