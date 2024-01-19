def solution(x):
    digit_sum = sum(list(map(int, str(x))))
    if x % digit_sum == 0:
        return True
    else:
        return False