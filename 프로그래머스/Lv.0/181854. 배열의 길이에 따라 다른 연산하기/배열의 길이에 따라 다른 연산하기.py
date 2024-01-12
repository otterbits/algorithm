def solution(arr, n):
    arr_len = len(arr)
    if arr_len % 2 == 1:
        for i in range(0, arr_len, 2):
            arr[i] += n
    else:
        for i in range(1, arr_len, 2):
            arr[i] += n
                       
    return arr