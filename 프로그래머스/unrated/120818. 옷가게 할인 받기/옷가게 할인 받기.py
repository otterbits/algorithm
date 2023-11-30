import math

def solution(price):
    answer = 0
    if price < 100000:
        price == price
    if 300000 > price >= 100000:
        price -= price * 0.05
    elif 500000 > price >= 300000:
        price -= price * 0.1
    elif price >= 500000:
        price -= price * 0.2
    answer = int(price)
    return answer