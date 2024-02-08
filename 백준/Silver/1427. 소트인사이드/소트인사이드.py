n = input()
list_n = []

for i in range(len(n)):
   list_n.append(n[i])

list_n = sorted(list_n, reverse=True)

for j in list_n:
   print(j, end= '')