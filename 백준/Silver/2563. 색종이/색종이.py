import sys
n = int(sys.stdin.readline().rstrip())

paper = [[0]*100 for _ in range(100)]

for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    for i in range(10):
        for j in range(10):
            paper[x+i][y+j] = 1

confetti_sum = 0
for i in paper:
    confetti_sum += sum(i)

print(confetti_sum)