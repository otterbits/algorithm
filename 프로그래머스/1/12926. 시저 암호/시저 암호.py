def solution(s, n):
    answer = ''
    for i in s:
        if i == " ":
            answer += i
        elif i.isupper():
            answer += chr(ord("A") + ((ord(i) + n - ord("A")) % 26))
        elif i.islower():
            answer += chr(ord("a") + ((ord(i) + n - ord("a")) % 26))
    return answer