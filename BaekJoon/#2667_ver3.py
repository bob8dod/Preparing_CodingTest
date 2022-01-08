# 단지 번호 붙이기 _ 60min
"""
DFS로 푼 버전.
먼저 DFS가 한번이 아닌 여러 번 진행해야 하기 때문에 solution함수에서 반복문을 통해
모든 요소에 접근하도록 한 후 방문했는지, 1인지를 판단하여 DFS 진행, 그 결과를 result에 누적
ver2에서 cnt를 global 변수로 선언함으로써
cnt를 따로 인자로 보내주지 않고 노드들끼리 실시간으로 공유하는 상황
개념적으로 접근이 더 편하긴함
"""
h_map = []
visited = []
di = [0,0,-1,1]
dj = [1,-1,0,0]


def dfs(i,j):
    global cnt
    cnt+=1
    visited[i][j]=1
    for tem_i,tem_j in zip(di,dj):
        ni, nj = i + tem_i, j + tem_j
        if 0<=ni<N and 0<=nj<N:
            if visited[ni][nj] == 0 and h_map[ni][nj] == 1:
                dfs(ni,nj)
                #return cnt -> 이건 끊기지 않고 한번에 연결하는 방법 찾기임
    return


def solution():
    global N, cnt
    N = int(input())
    for i in range(N):
        h_map.append(list(map(int, list(input()))))
        visited.append([0 for _ in range(N)])

    result = []
    for i in range(N):
        for j in range(N):
            if h_map[i][j] == 1 and visited[i][j] == 0:
                cnt = 0
                dfs(i, j)
                result.append(cnt)

    print(len(result))
    for i in sorted(result): print(i)
    return

solution()
