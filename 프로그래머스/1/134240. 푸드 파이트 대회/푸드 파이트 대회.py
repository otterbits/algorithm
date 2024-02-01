def solution(food):
    answer = ''
    for i in range(1, len(food)):
        answer += str(i) * (int(food[i]) // 2)
    answer += '0'
    answer += answer[len(answer)-2::-1]
    return answer