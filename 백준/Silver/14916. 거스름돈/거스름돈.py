import sys
input = sys.stdin.readline

n = int(input())
cnt = 0

while True:
    if n == 1 or n == 3:
        print(-1)
        break
    if n % 5 == 0:
        print(n // 5)
        break
    else:
        n -= 2
        cnt += 1
        if n % 5 == 0:
            cnt += n // 5
            print(cnt)
            break