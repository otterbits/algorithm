import sys
human = []
n = int(sys.stdin.readline())
result = [1] * n


for _ in range(n):
    human.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    count = 0
    for j in range(n):
        if human[j][0] > human[i][0] and human[j][1] > human[i][1]:
            count += 1
    result[i] += count

for k in result:
    print(k, end= " ")