def solution(myString, pat):
    if pat.upper() in myString.upper():
        return 1
    else:
        return 0