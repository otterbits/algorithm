def solution(n):
    answer = ''
    while n > 0:
        remain = n % 3
        n = n // 3
        answer += str(remain)
    return int(answer,3)