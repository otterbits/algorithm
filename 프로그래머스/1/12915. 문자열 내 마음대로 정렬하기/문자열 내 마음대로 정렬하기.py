def solution(strings, n):
    result = sorted(strings, key=lambda x:(x[n],x))
    return result