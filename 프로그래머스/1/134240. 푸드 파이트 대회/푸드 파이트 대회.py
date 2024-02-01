def solution(food):
    answer = ''
    for i in range(1, len(food)):
        answer += str(i) * (int(food[i]) // 2)
    rev = answer[::-1]
    return answer + '0' + rev