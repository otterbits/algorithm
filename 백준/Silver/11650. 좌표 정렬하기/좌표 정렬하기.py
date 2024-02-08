n = int(input())
list_n = []

for i in range(n):
   a, b = map(int, input().split())
   list_n.append([a,b])

list_n = sorted(sorted(list_n, key=lambda x : x[1]))

for x, y in list_n:
   print(f'{x} {y}')