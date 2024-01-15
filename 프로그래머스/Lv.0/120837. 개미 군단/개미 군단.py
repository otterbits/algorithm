def solution(hp):
    answer = 0
    general_attack = 5
    solider_attack = 3
    work_attack = 1

    while hp > 0:
        if hp >= general_attack:
            answer += hp // general_attack
            hp %= general_attack
        elif hp >= solider_attack:
            answer += hp // solider_attack
            hp %= solider_attack
        if hp >= work_attack:
            answer += hp // work_attack
            hp %= work_attack
            
    return answer