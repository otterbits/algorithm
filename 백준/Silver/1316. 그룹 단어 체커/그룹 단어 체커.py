n = int(input())

for i in range(n):
    words = input()
    for j in range(len(words) - 1):
        if words[j] == words[j+1]:
            continue
        elif words[j] in words[j+1:]:
            n -= 1
            break

print(n)