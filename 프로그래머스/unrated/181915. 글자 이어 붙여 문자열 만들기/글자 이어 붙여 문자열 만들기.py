def solution(my_string, index_list):
    answer = ''
    for n in index_list:
        answer += my_string[n]
    return answer