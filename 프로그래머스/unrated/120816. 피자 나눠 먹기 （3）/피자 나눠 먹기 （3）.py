def solution(slice, n):
    for i in range(0,201):
        if slice * i >= n:
            return i