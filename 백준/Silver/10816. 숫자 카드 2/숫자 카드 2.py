import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
needs = list(map(int, input().split()))

# cards.sort()
cards_cnt = {}

for card in cards:
    if card not in cards_cnt:
        cards_cnt[card] = 1
    else:
        cards_cnt[card] += 1

for need in needs:
    result = cards_cnt.get(need)
    if result:
        print(cards_cnt[need], end=" ")
    else:
        print(0, end=" ")