# BaekJoon P15686 치킨거리 (구현, 완전탐색 | Gold5)
"""
[실수]
map이면 dfs,bfs로 조져야겠다는 생각에 갖혔음
dfs,bfs로 해야겠다 생각하니 전수조사는 시간복잡도상 불가능하다 생각하여 Greedy로 생각하게 됨

[부족한 점]
map -> dfs,bfs 라는 생각 버리기
일반 거리 계산은 그냥 abs로 뺄셈으로 때려버려서 진행가능!

[풀이]
combination을 통해 해당 조건에 맞는 조합을 구해주고
각 조합(경우)마다의 최소 통합치킨거리를 구해주는 단순한 문제
먼저 house의 위치, chicken store의 위치를 기억한다음
각각의 경우에 대해서 그 거리만을 구하면 됨 (거리 = abs(h[0]-c[0])+abs(h[1]-c[1]))

각 house에 대해서 최소 치킨 거리를 구한후
그들의 합의 최소 총합 치킨 거리를 가지고 있는 case를 구하는 것

"""
import sys
from itertools import combinations

def solution(n,m,gmap):
    house = []
    store = []
    for i in range(n):
        for j in range(n):
            if gmap[i][j] == 1: house.append([i,j])
            elif gmap[i][j] == 2: store.append([i,j])

    total_dis = sys.maxsize
    for case in combinations(store, m):
        total_temp = 0
        for h in house:
            distance = sys.maxsize
            for c in case:
                distance = min(distance, abs(c[0]-h[0])+abs(c[1]-h[1]))
            total_temp+=distance
        total_dis = min(total_dis, total_temp)

    return total_dis

if __name__ == '__main__':
    N, M = map(int,input().split())
    gmap = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    print(solution(N, M, gmap))
