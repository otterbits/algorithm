import sys
input = sys.stdin.readline

x = int(input())
# d에 숫자 1이 되는 데 필요한 연산의 최솟값을 저장해준다. n + 1은 1번째 수는 d[1]이 아닌 d[2]이기 때문이다.
d = [0] * (x + 1)


for i in range(2, x + 1):
    # d[i - 1](i - 1이 1이 되는데 필요한 최소한의 연산) + 1(i에서 1을 빼서 i - 1이 되는데 필요한 연산 횟수 1회)
    d[i] = d[i - 1] + 1
    if i % 2 == 0:
        # 나눈 값에 1을 더하는 이유는 계산한 횟수를 저장해야하기 때문
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)

print(d[x])