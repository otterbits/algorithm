import sys

n = int(sys.stdin.readline())
numbers = list(sys.stdin.readline().rstrip())
sum_n = 0

for i in numbers:
    sum_n += int(i)

print(sum_n)