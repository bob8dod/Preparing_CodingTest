# 전쟁-전투 _30min
"""
이전에도 많이 풀었던 문제. BFS로 해결.
W와B 두가지로 구분하여 둘이 따로 count해줌.

중요!
# N과 M이 세로인지 가로인지 주의하지 않아 시간지체됨
# 내가 갈 수 있는 애들에 대해 탐색하고 Q에 넣어줄때, visited를 표시해줘야됨
# 안그러면 BFS이기에 겹치는 놈들이 있을 수 있음!!!!
"""
from collections import deque
N, M = map(int, input().split())
war = [[j for j in list(input())] for _ in range(M)]
visited = [[0 for _ in range(N)] for _ in range(M)]

di = [0,0,-1,1]
dj = [1,-1,0,0]

def bfs(i,j,c):
    cnt = 0
    Q = deque([[i,j]])
    visited[i][j] = 1
    while Q:
        curr = Q.popleft()
        cnt+=1
        for ti, tj in zip(di,dj):
            ni = curr[0]+ti
            nj = curr[1]+tj
            if c == 'W':
                if 0 <= ni < M and 0<= nj < N and not visited[ni][nj] and war[ni][nj]=='W':
                    Q.append([ni,nj])
                    visited[ni][nj] = 1
            else:
                if 0 <= ni < M and 0<= nj < N and not visited[ni][nj] and war[ni][nj]=='B':
                    Q.append([ni,nj])
                    visited[ni][nj] = 1

    return cnt*cnt

def solution(N,M):
    cnt_w = 0
    cnt_b = 0
    for i in range(M):
        for j in range(N):
            if visited[i][j] == 1: continue
            if war[i][j] == 'W': cnt_w+= bfs(i, j, 'W')
            else: cnt_b+= bfs(i,j,'B')

    return cnt_w, cnt_b

print(*solution(N,M))
