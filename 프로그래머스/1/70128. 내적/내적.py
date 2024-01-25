def solution(a, b):
    answer = 0
    for a_int, b_int in zip(a,b):
        answer += a_int * b_int
    return answer