n = int(input())
list_n = []

for i in range(n):
   age, name = input().split()
   list_n.append([age, name, i])

list_n = sorted(sorted(list_n, key=lambda x: x[2]), key=lambda x: int(x[0]))

for age, name, n in list_n:
   print(f'{age} {name}')