import sys
n = int(sys.stdin.readline())
devil = 666
count = 0

while True:
    if '666' in str(devil):
        count += 1
    if count == n:
        break
    devil += 1

print(devil)