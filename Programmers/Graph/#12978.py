# 12978 배달
from collections import defaultdict
import heapq

gmap = defaultdict(list)
result = []
# visited = []
"""
결론적으로 basic 다익스트라
"단방향, 노드간의 간선은 단 하나"의 기본적인 다익스트라와
"양방향, 노드간의 간선은 여러 개"의 향상된 다익스트라는 결국 수행되는 알고리즘은 같음.
즉, 기본적인 다익스트라의 알고리즘이 향상된 다익스트라의 추가적인 케이스들도 처리한다는 뜻.
"""
def dja(start):
    Q = [[0,start]]
    result[start] = 0
    while Q:
        curr_dis, curr_idx = heapq.heappop(Q)
        # visited[curr_idx] = 1
        if curr_dis > result[curr_idx] : continue
        for next_idx, next_dis in gmap[curr_idx]:
            # if visited[next_idx]: continue
            total_dis = curr_dis + next_dis
            if result[next_idx] > total_dis:
                result[next_idx] = total_dis
                heapq.heappush(Q, [total_dis,next_idx])

def solution(N, roads, K):
    global result, visited, gmap
    result = [500001 for _ in range(N+1)]
    # visited = [0 for _ in range(N+1)]

    for road in roads:
        a, b, d = road
        gmap[a].append([b,d])
        gmap[b].append([a,d])

    dja(1)

    answer = 0
    for i in result:
        if i <= K: answer+=1

    return answer
