def solution(arr, delete_list):
    for i in list(arr):
        if i in delete_list:
            arr.remove(i)
            
    return arr