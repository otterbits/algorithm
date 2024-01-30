def solution(s):
    answer = ''
    words = s.split(" ")
    for word in words:
        part = ''
        for i in range(len(word)):
            if i % 2 == 0:
                part += word[i].upper()
            else:
                part += word[i].lower()
        answer += (part + ' ')
    return answer[0:-1]