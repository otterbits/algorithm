def solution(price, money, count):
    usage = 0
    for i in range(count+1):
        usage += price * i
    if usage - money > 0:
        return usage - money
    else:
        return 0