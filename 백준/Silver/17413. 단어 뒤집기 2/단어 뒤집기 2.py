"""
< 이걸 찾는다.
이떄까지 있던 거 거꾸로 출력한다.
> 이걸 찾을 때 까지 계속 넣는다.
> 이걸 찾으면 result에 통째로 넣는다.(초기화)

" "가 있는데, 괄호 밖이면 거꾸로 넣는다.

"""
import sys

string = sys.stdin.readline().rstrip() + ' '
stack = []
result = ''
bracket = False

for i in string:
    if i == "<":
        bracket = True
        result += ''.join(stack[::-1])
        stack = []
    stack.append(i)
    if i == ">":
        bracket = False
        result += ''.join(stack)
        stack = []
    if i == " " and not bracket:
        stack.pop()
        result += ''.join(stack[::-1])
        result += " "
        stack = []

print(result)
