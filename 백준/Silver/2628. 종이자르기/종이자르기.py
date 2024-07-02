import sys
input = sys.stdin.readline

width, height = map(int, input().split())

w = [0, width]
h = [0, height]

n = int(input())

for _ in range(n):
    order, length = map(int, input().split())
    if order == 0:
        h.append(length)
    else:
        w.append(length)
        
h.sort()
w.sort()

max_area = 0

for i in range(len(w) - 1):
    for j in range(len(h) - 1):
        point_width = w[i+1] - w[i]
        point_length = h[j+1] - h[j]
        max_area = max(point_width * point_length, max_area)

print(max_area)