def solution(s):
    if s.isdigit():
        if len(s) == 4 or len(s) == 6:
            return True
        else:
            return False
    else:
        return False