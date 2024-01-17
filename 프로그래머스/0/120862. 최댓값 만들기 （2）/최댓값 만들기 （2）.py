def solution(numbers):
    asending = sorted(numbers)
    return max(asending[0] * asending[1], asending[-1] * asending[-2])