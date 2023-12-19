def solution(my_string, alp):
    for i in my_string:
        if i == alp:
            my_string = my_string.replace(i, i.upper())
    return my_string