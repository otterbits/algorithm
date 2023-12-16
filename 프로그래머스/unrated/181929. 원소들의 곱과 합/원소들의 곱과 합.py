def solution(num_list):
    multi = 1
    square = sum(num_list) * sum(num_list)
    for i in num_list:
        multi *= i
    if multi > square:
        return 0
    else:
        return 1