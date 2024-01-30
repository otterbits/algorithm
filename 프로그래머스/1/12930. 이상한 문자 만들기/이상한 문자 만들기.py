def solution(s):
    answer = []
    words = s.split(" ")
    for word in words:
        part = []
        for i in range(len(word)):
            if i % 2 == 0:
                part.append(word[i].upper())
            else:
                part.append(word[i].lower())
        part = "".join(part)
        answer.append(part)
    answer=" ".join(answer)
    return answer