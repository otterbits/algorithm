def solution(left, right):
    answer = 0
    divisor = 0
    var_list = list(range(left,right+1))
    div_list = []
    for i in range(left, right+1):
        for j in range(1, i+1):
            if i % j == 0:
                divisor += 1
        div_list.append(divisor)
        divisor = 0
    for var, div in zip(var_list, div_list):
        if div % 2 == 0:
            answer += var
        else:
            answer -= var
    return answer