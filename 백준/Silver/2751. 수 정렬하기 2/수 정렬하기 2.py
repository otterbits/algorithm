import sys
input = sys.stdin.readline

n = int(input())
list_n = []

for i in range(n):
    num = int(input())
    list_n.append(num)

for i in sorted(list_n):
    print(i)