# BaekJoon P16234 인구이동 (BFS, 구현 | Gold5)
"""
[실수]

[부족한 점]
차근차근 하나를 해결하고 넘어가야 되는데
계속 하나 해결하기도 전에 다음으로 넘어가서 코딩을 진행함
차근차근 하자

[풀이]
쉽게 생각하면 땅따먹기
->  모든 위치에 대해서 국경선을 열수 있는지 판단하는데
    이때 한 위치에 대해서 국경선을 열 수 있는 애들을 모두 서치함
    => bfs. 바이러스가 퍼지듯이!

하루를 기준으로 반복 -> while True
각각의 위치에 대해서 방문되지 않았다면 bfs 실시 -> (한 위치에 대해서 국경선을 열 수 있는 애들을 모두 서치)
bfs에서 서치가 진행되었다면 1 아니면 0 -> 하루를 기준으로 한번이라도 서치가 진행되었다면 다음날로 아니라면 그대로 종료
또한 각 bfs에서 gmap 갱신까지 진행.
"""

import sys
from collections import deque

di = [[0,1],[1,0],[0,-1],[-1,0]]

def bfs(n,l, r, i,j,visited,gmap):
    q = deque([[i,j]])
    check = []
    result = 0
    while q:
        ci, cj = q.popleft()
        check.append([ci,cj])
        result += gmap[ci][cj]
        for ti, tj in di:
            ni, nj = ci+ti, cj+tj
            if (0<=ni<n and 0<=nj<n) and not visited[ni][nj]\
                    and l<=abs(gmap[ci][cj] - gmap[ni][nj])<=r:
                visited[ni][nj] = 1
                q.append([ni,nj])

    if len(check) == 1: return 0
    else:
        avg = result//len(check)
        for ki,kj in check:
            gmap[ki][kj] = avg
        return 1

def solution(n, l, r, gmap):
    answer = 0
    while True:
        visited = [[0 for _ in range(n)] for _ in range(n)]
        check = 0
        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    visited[i][j] = 1
                    if bfs(n,l, r, i,j,visited,gmap) : check = 1
        if check: answer += 1
        else: break

    return answer


if __name__ == '__main__':
    N, L, R = map(int,input().split())
    gmap = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    print(solution(N, L, R, gmap))
