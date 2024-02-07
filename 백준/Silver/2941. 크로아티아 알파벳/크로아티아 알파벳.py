croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = input()
count = len(word)

for i in croatia:
    if i in word:
        count -= word.count(i)

print(count)
