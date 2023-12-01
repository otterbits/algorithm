def solution(n):
    answer = 0
    if n % 2 == 1:
        for i in range(n+1):
            if 2*i+1 <= n:
                answer += 2*i+1
    else:
        for i in range(n+1):
            if 2*i <= n:
                answer += (2*i) ** 2
    return answer
