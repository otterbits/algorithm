import sys
input = sys.stdin.readline

N = int(input())
lst = []

for _ in range(N):
    number = int(input())
    lst.append(number)


print(*sorted(lst), sep='\n')