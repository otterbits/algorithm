def solution(ineq, eq, n, m):
    if eq == "!":
        if ineq == ">":
            if n > m:
                return 1
            elif n <= m:
                return 0
        elif ineq == "<":
            if n < m:
                return 1
            elif n >= m:
                return 0
    elif eq == "=":
        if ineq == ">":
            if n >= m:
                return 1
            elif n < m:
                return 0
        elif ineq == "<":
            if n <= m:
                return 1
            elif n > m:
                return 0