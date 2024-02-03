def solution(n, arr1, arr2):
    answer = []
    arr1_answer = []
    arr2_answer = []
    
    for i, j in zip(arr1, arr2):
        arr1_answer.append(format(i, '0' + str(n) + 'b'))
        arr2_answer.append(format(j, '0' + str(n) + 'b'))

    for a in range(n):
        code = ''
        for b in range(n):
            if arr1_answer[a][b] == '1' or arr2_answer[a][b] == '1':
                code += "#"
            else:
                code += ' '
        answer.append(code)
    return answer


"""
풀이과정

1. arr1, arr2를 다 돌면서 2진수로 만들어준다.
2. answer_arr1, answer_arr2에 추가해준다.
3. 두 개를 같은 인덱스에서 비교한다.
4-1. 1이 하나라도 있으면 #
4-2. 없으면 ' '을 answer에 추가한다.
"""