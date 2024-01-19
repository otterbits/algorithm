def solution(n):
    list_N = sorted(list(map(int, str(n))), reverse=True)
    return int(''.join(map(str, list_N)))