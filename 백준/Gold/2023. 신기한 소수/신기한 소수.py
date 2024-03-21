import sys

N = int(sys.stdin.readline().strip())


# 소수 판별
def is_prime_number(x):
    # 가운데 약수 기준으로 대칭
    for i in range(2, int(x ** 0.5 + 1)):
        if x % i == 0:
            return False
    return True


def dfs(n):
    # 해당 자릿수면 출력
    if len(str(n)) == N:
        print(n)
    else:
        # 자릿수 변동
        for i in range(10):
            if is_prime_number(n * 10 + i):
                dfs(n * 10 + i)


# 소수 4개 대입
dfs(2)
dfs(3)
dfs(5)
dfs(7)
