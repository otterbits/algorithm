def digit(n):
    return n + sum(map(int, str(n)))


number = list(range(1, 10001))

for i in range(1, 10001):
    if digit(i) in number:
        number.remove(digit(i))

for j in number:
    print(j)
