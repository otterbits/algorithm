def solution(s):
    answer = []
    index = {}
    for i in range(len(s)):
        if s[i] not in index:
            answer.append(-1)
            index[s[i]] = i
        else:
            answer.append(i - index[s[i]])
            index[s[i]] = i
    return answer

            # s를 한 글자씩 돌면서 index도 같이 검색
            # 만약, 해당 글자가 처음 나타난 거면 -1을 append,
            # 두 번 이상 나타난 거면 해당 글자 왼쪽 첫 번째 글자 index를 뺀 값을 append,