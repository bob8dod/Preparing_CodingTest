# 1926 그림 _ 18min
"""
이전에 풀었던 DFS/BFS랑 똑같은 유형의 문제
"""

import sys
from collections import deque

n,m = map(int,input().split())
page = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
di = [0,0,1,-1]
dj = [1,-1,0,0]
visited = [[0 for _ in range(m)] for _ in range(n)]

def bfs(i,j):
    Q = deque([[i,j]])
    cnt = 0
    while Q:
        curr = Q.popleft()
        cnt += 1
        for ii,jj in zip(di,dj):
            ni = curr[0] + ii
            nj = curr[1] + jj
            if 0<=ni<n and 0<=nj<m:
                if not visited[ni][nj] and page[ni][nj] == 1:
                    visited[ni][nj] = 1
                    Q.append([ni,nj])

    return cnt

def solution():
    max_cnt = 0
    total = 0
    for i in range(n):
        for j in range(m):
            if page[i][j] == 1 and visited[i][j] == 0:
                total+=1
                visited[i][j] = 1
                curr_cnt = bfs(i,j)
                if curr_cnt> max_cnt : max_cnt = curr_cnt

    print(total)
    print(max_cnt)

solution()
