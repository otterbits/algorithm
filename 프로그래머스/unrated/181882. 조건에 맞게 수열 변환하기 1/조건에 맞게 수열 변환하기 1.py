def solution(arr):
    answer = []
    for i in arr:
        if i % 2 == 1 and i < 50:
            i = i * 2
        elif i % 2 == 0 and i >= 50:
            i = i / 2
        else:
            i = i
        answer.append(i)
    return answer