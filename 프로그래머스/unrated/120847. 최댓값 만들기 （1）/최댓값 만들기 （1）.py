def solution(numbers):
    answer = 0
    numbers.sort()
    length = len(numbers)
    answer = numbers[length-1] * numbers[length-2]
    return answer