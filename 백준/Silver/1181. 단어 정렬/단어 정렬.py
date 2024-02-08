n = int(input())
list_word = []

for i in range(n):
    word = input()
    list_word.append(word)

list_word = sorted(sorted(set(list_word)), key=len)

for i in list_word:
    print(i)