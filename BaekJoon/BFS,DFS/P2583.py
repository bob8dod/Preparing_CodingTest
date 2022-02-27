# 백준 P2583 영역 구하기 _ 26min
"""
먼저 visited에 표시 후 bfs 조져버리기
항상 bfs할 때 visited 체크해주는 것 조심!
"""
from collections import deque

I, J, K = map(int, input().split())
li = [list(map(int,input().split())) for _ in range(K)]
visited = [[0 for _ in range(J)] for _ in range(I)]
di = [0,1,0,-1]
dj = [1,0,-1,0]

def bfs(i,j):
    Q = deque([[i,j]])
    width = 0
    while Q:
        ci, cj = Q.popleft()
        width+=1
        for ti, tj in zip(di,dj):
            ni = ci + ti
            nj = cj + tj
            if (0<=ni<I and 0<=nj<J) and not visited[ni][nj]:
                visited[ni][nj] = 1
                Q.append([ni,nj])

    return width

def solution(li):
    for l in li:
        sj, si, ej, ei = l
        # l[0],l[1],l[2]-1,l[3]-1
        for i in range(si,ei):
            for j in range(sj,ej):
                visited[i][j] = 1

    cnt = 0
    width = []
    for i in range(I):
        for j in range(J):
            if visited[i][j] == 0:
                visited[i][j] = 1
                width.append(bfs(i,j))
                cnt += 1

    print(cnt)
    for i in sorted(width):
        print(i, end=' ')

solution(li)
