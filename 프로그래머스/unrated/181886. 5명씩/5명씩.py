def solution(names):
    answer = []
    for n in range(len(names)):
        if 5 * n < len(names):
            answer.append(names[5*n])
        
    return answer