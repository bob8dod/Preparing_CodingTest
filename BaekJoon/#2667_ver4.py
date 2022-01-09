# 단지 번호 찾기 _ Using Queue
"""
bfs로 푼 버전.
내가 갈 수 있는 모든 노드들에 대해서 Q에 저장한다음
bfs로 Q.popleft()로다가 하나씩 접근하는 것
여기서 중요한 점은 현재 노드에서 갈 수 있는 모든 노드들을 저장할 때
visited에 추가해줘야됨. 그렇지 않으면 겹치는 현상 발생
"""

from collections import deque
h_map = []
visited = []
di=[0,0,-1,1]
dj=[1,-1,0,0]
Q=deque()

def bfs():
    cnt = 0
    while Q:
        cnt+=1
        i,j = Q.popleft()
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0<=ni<N and 0<=nj<N:
                if h_map[ni][nj] == 1 and visited[ni][nj] == 0:
                    Q.append([ni,nj])
                    visited[ni][nj] = 1
    return cnt

def solution():
    global N
    N = int(input())
    for _ in range(N):
        h_map.append(list(map(int,list(input()))))
        visited.append([0 for _ in range(N)])

    result=[]
    for i in range(N):
        for j in range(N):
            if 0<=i<N and 0<=j<N:
                if h_map[i][j]==1 and visited[i][j]==0:
                    Q.append([i,j])
                    visited[i][j] = 1
                    result.append(bfs())

    print(len(result))
    for i in sorted(result): print(i)
