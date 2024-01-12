def solution(numbers, n):
    result = 0
    for i in numbers:
        result += i
        if result > n:
            return result