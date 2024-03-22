import sys
input = sys.stdin.readline

def is_prime_number(x):
    for i in range(2, int(x ** 0.5 + 1)):
        if x % i == 0:
            return False
    return True

# 자릿수
N = int(input())


def dfs(num):
    # 자릿수와 같으면 출력해라
    if len(str(num)) == N:
        print(num)
        return
    else:
        for i in range(1, 10):
            # 다음 자릿수 구하는 것
            next_digit = num * 10 + i
            # 소수면 자릿수 비교해라
            if is_prime_number(next_digit):
                dfs(next_digit)


# 일의 자릿수일 때 소수인 4개의 숫자
dfs(2)
dfs(3)
dfs(5)
dfs(7)