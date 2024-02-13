import sys
n = int(sys.stdin.readline())
sg_number = set(map(int, (sys.stdin.readline().split(' '))))

m = int(sys.stdin.readline())
card_number = list(map(int, (sys.stdin.readline().split(' '))))

for i in card_number:
    if i in sg_number:
        print('1', end=' ')
    else:
        print('0', end=' ')
