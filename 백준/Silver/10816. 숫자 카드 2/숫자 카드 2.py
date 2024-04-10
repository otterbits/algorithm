import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
needs = list(map(int, input().split()))

cards.sort()

for need in needs:
    left_index = bisect_left(cards, need)
    right_index = bisect_right(cards, need)
    print(right_index - left_index)