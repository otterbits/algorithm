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