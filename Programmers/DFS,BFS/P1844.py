# 찾아라 프로그래밍 마에스터 게임 맵 최단 거리 P1844
"""
실수: visited는 필요 없었음. 애초에 dp로 기존 값보다 작은 애일 경우만 bfs를 뻗어나감.
그럼, 기존에 훑어왔던 애들에 대해서는 당연히 dp값이 크기 때문에 (왕복과 같은 개념) 걸로 뻗어나가지 않아, visited와 같은 역할을 함
더욱이 visited를 사용하면 안됨 -> 기존의 값과 비교해서 더 작은 경우 교체해 줘야 되는데, visited를 사용하게 되면 접근조차 하지 못하게 됨

풀이: bfs, dp 사용. bfs로 4방향으로 뻗어나가면서 기존에 구했던 dp 값보다 작으면 값을 교체하면서 그 자체로 bfs를 또 뻗어나감
마지막 값이 교체 되었으면 (갱신, 도달했다는 뜻) 그 dp 값을 반환하고 교체되지 않았다면(도달할 수 없는 상황) -1 반환
"""

import sys
from collections import deque

def bfs(maps, dp, n, m):
    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    q = deque([[0,0,1]])
    while q:
        i,j,cnt = q.popleft()
        for di,dj in d:
            ni, nj = i+di, j+dj
            if (0<=ni<n and 0<=nj<m) and maps[ni][nj] != 0:
                if dp[ni][nj] > cnt + 1:
                    dp[ni][nj] = cnt + 1
                    q.append([ni,nj,cnt+1])

def solution(maps):
    n, m = len(maps), len(maps[0])
    dp = [[sys.maxsize for _ in range(m)] for _ in range(n)]
    bfs(maps, dp, n, m)
    return dp[n-1][m-1] if dp[n-1][m-1] != sys.maxsize else -1
