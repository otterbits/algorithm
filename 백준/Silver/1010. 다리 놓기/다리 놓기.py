import sys
import math

cnt = int(sys.stdin.readline())
for _ in range(cnt):
    n, m = map(int,sys.stdin.readline().split(' '))
    print(math.comb(m, n))