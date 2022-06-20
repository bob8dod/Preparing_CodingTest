# BaekJoon P1916 최소비용 구하기 (다익스트라 | Gold5)
"""
[실수]
단방향 그래프인데, 양방향으로 구해서 시간 낭비

[부족한 점]
알고리즘을 응용할 수 는 있지만, 확실히 어떤 원리로 동작하는 지 모르고 풀었음

[풀이]
한마디로 그냥 다익스트라 (출발점에서 도착점까지의 최단거리이므로)
문제에 따라 그래프(단방향)를 완성해 준 후
시작점을 지정하여 다익스트라 실행

다익스트라 -> 더 작은 값에 우선순위를 주는 알고리즘
"""

import heapq
import sys
from collections import defaultdict

def dja(start,gmap,result):
    Q = [[0,start]] # [[비용, 현재 노드]]
    result[start] = 0
    while Q:
        curr_dis, curr_idx = heapq.heappop(Q) # 가장 작은 비용 pop -> 우선순위 Q
        if curr_dis > result[curr_idx] : continue # 순서가 돌아오는 동안, 더 작은 값을 찾은 경우
        for next_idx, next_dis in gmap[curr_idx]:
            total_dis = curr_dis + next_dis
            if result[next_idx] > total_dis:
                result[next_idx] = total_dis # 더 작은 값으로 교체
                heapq.heappush(Q, [total_dis,next_idx]) # 우선순위 Q 추가

def solution(n, roads,start,end):
    result = [sys.maxsize for _ in range(n+1)]
    gmap = defaultdict(list)

    for road in roads:
        a, b, d = road
        gmap[a].append([b,d])

    dja(start,gmap,result)

    return result[end]

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())
    roads = [list(map(int,sys.stdin.readline().split())) for _ in range(m)]
    start, end = map(int, sys.stdin.readline().split())

    print(solution(n,roads,start,end))
