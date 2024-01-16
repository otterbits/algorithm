# 문제 잘못됨 idx보다 '같거나 큰'임
def solution(arr, idx):
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i
    return -1
            