def solution(array, commands):
    answer = []
    for command in commands:
        array_sorted = sorted(array[command[0]-1:command[1]])
        print(array_sorted)
        answer.append(array_sorted[command[2]-1])
    return answer

"""
commands를 하나씩 빼와서
0, 1번째로 array 정렬
2번째로 숫자 뽑기
"""