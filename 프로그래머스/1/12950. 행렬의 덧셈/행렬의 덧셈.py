def solution(arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        row = []
        for a, b in zip(i, j):
            row.append(a+b)
        answer.append(row)
    return answer