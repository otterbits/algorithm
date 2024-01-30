def solution(d, budget):
    answer = 0
    d = sorted(d)
    for i in d:
        budget -= i
        if budget >= 0:
            answer += 1
    return answer