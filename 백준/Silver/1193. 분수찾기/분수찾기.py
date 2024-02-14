import sys
n = int(sys.stdin.readline())
line = 1
while n > line:
    n -= line
    line += 1

if line % 2 == 0:
    print(n, "/", line - n + 1, sep="")
else:
    print(line - n + 1, "/", n, sep="")