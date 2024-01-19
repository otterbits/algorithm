def solution(n):
    if float(n**(1/2)).is_integer():
        return (n**(1/2)+1)**2
    else:
        return -1