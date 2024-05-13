import sys
import heapq
input = sys.stdin.readline
# 무한을 의미하는 값 설정
INF = int(1e9)

# 정점(vertex), 간선(edge) 개수 받기
v, e = map(int, input().split())
# 시작 정점
start = int(input())
# 각 정점에 연결되어 있는 정점에 대한 정보를 담는 리스트 생성
graph = [[] for i in range(v + 1)]
# 최단 거리 테이블 무한으로 초기화
distance = [INF] * (v + 1)
# 시작점에서 시작점까지의 거리는 0
distance[start] = 0

for _ in range(e):
    # st에서 ed까지 가중치 dist만큼 걸린다.
    st, ed, dist = map(int, input().split())
    graph[st].append((dist, ed))

q = []
# 우선순위 큐에 시작점과 거리 삽입
# 최단 거리의 우선 순위를 생각해야하기 때문에 최단 거리를 첫번째로 설정한다
heapq.heappush(q, (distance[start], start))
# 큐가 비어있지 않다면
while q:
    # 현재 정점에서 가장 최단 거리가 짧은 정점에 대한 정보 꺼내기
    dist, now = heapq.heappop(q)
    # 현재 정점 이미 처리된 적이 있는 정점이라면 무시(최단 거리보다 거리가 길 경우 굳이 넣을 필요가 없다)
    if distance[now] < dist:
        continue
    # 현재 정점과 연결된 다른 인접한 정점들을 확인
    for i in graph[now]:
        # 현재 정점을 거쳐 다른 정점으로 이동하는 거리가 짧은 경우,
        if dist + i[0] < distance[i[1]]:
            # 최단 거리 갱신
            distance[i[1]] = dist + i[0]
            # 큐에 최단 거리 정점 삽입
            heapq.heappush(q, (dist + i[0], i[1]))

for i in range(1, v + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])