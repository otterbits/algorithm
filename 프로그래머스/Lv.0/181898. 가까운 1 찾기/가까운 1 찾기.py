# 문제 잘못됨 idx보다 '같거나 큰'임
def solution(arr, idx):
    ans = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            ans = i
            if ans >= idx:
                return ans
    return -1
            