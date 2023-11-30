def solution(money):
    answer = []
    count = 0
    remain = 0
    ice_coffee = 5500
    count = money // ice_coffee
    remain = money % ice_coffee
    answer.append(count)
    answer.append(remain)
    return answer