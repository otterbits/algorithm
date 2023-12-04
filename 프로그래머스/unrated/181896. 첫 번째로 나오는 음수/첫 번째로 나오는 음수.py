def solution(num_list):
    answer = 0
    for i in num_list:
        if i < 0:
            return num_list.index(i)
        else:
            answer = -1
    return answer