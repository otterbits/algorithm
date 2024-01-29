def solution(arr):
    answer = []
    left = arr[0]
    for i in arr:
        if i != left:
            answer.append(left)
            left = i
    answer.append(arr.pop())
    return answer