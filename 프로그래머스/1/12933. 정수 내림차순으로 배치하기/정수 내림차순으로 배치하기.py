def solution(n):
    list_N = sorted(list(str(n)), reverse=True)
    return int(''.join(list_N))