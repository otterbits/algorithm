def solution(t, p):
    answer = 0
    
    for i in range(len(t)):
        if int(t[i:i+len(p)]) <= int(p):
            if len((t[i:i+len(p)])) == len(p):
                answer += 1
    return answer