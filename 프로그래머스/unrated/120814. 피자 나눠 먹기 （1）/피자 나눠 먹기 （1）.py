def solution(n):
    for i in range(1, 16):
        if 7*i // n >= 1:
            return i