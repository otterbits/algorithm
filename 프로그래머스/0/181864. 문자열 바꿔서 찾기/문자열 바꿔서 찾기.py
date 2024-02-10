def solution(myString, pat):
    newString = ""
    for i in range(len(myString)):
        if myString[i] == "A":
            newString += "B"
        else:
            newString += "A"
    if pat in newString:
        return 1
    else:
        return 0
