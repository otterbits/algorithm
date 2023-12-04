def solution(num_list):
    answer = num_list
    length = len(num_list)
    
    if num_list[length-1] > num_list[length-2]:
        answer.append(num_list[length-1] - num_list[length-2])
    elif num_list[length-1] <= num_list[length-2]:
        answer.append(num_list[length-1] * 2)
    return answer