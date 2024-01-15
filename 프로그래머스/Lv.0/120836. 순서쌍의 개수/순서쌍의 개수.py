def solution(n):
    answer = 0
    for i in range(1, n+1):
        if (n / i).is_integer():
            answer += 1
    return answer