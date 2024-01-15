def solution(my_string):
    gather = ['a', 'e', 'i', 'o', 'u']
    for i in my_string:
        if i in gather:
            my_string = my_string.replace(i, '')
    return my_string