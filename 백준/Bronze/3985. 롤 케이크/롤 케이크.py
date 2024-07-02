import sys
input = sys.stdin.readline

length = int(input())
num = int(input())
arr = [0] * (length)
expect_arr = [0]
cnt_arr = [0]

for n in range(1, num + 1):
    start, end = map(int, input().split())
    expect_arr.append(end - start + 1)
    for i in range(start - 1, end):
        if arr[i] == 0:
            arr[i] = n
        else:
            continue
    cnt_arr.append(arr.count(n))

print(expect_arr.index(max(expect_arr)))
print(cnt_arr.index(max(cnt_arr)))
