import sys
input = sys.stdin.readline

N = input()
lst = set(map(int, input().split()))
M = input()
num = list(map(int, input().split()))

for i in num:
    if i in lst:
        print(1)
    else:
        print(0)
