import sys

# 출력값 받기
S = sys.stdin.readline().strip()
# 알파벳 카운트 리스트
alphabet = [0] * 26

for i in S:
    # 출력값 한 글자씩 확인 후 ord로 index 구한 후, 1씩 더해주기 (소문자로만 이루어져 있으므로)
    alphabet[ord(i) - ord("a")] += 1

# list 한 번에 출력
print(*alphabet)
