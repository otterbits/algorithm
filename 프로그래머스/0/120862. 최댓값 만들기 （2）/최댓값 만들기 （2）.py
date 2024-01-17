def solution(numbers):
    asending = sorted(numbers)
    front = asending[-2:]
    front_answer = back_answer = 1
    back = asending[:2]
    for i in front:
        front_answer *= i
    for j in back:
        back_answer *= j
    return max(front_answer, back_answer)