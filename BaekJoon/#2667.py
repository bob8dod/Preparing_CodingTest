# 단지 번호 붙이기 _ 60min
"""
DFS로 푼 버전.
먼저 DFS가 한번이 아닌 여러 번 진행해야 하기 때문에 solution함수에서 반복문을 통해
모든 요소에 접근하도록 한 후 방문했는지, 1인지를 판단하여 DFS 진행, 그 결과를 result에 누적
DFS가 이루어지는 부분에서는 연결되어 더 나아가는 상황에서 1씩 더함.
즉, tree형식으로 보자면 자식노드로 연결되는 그 선이 '+'연산이라고 생각하면됨
그 후 해당 노드가 조건에 맞다면 1.
즉, 부모노드의 자식노드가 모두 조건에 맞지 않는다면 
재귀형식으로 leaf에서 root까지 누적합 연산 진행됨.
! dfs로 들어오는 그 해당 노드를 자식노드가 아닌 부모노드로 봐야되는 것이 핵심!
"""

h_map = []
visited = []
di = [0,0,-1,1]
dj = [1,-1,0,0]


def dfs(i,j):
    visited[i][j]=1
    cnt=1
    for tem_i,tem_j in zip(di,dj):
        ni, nj = i + tem_i, j + tem_j
        if 0<=ni<N and 0<=nj<N:
            if visited[ni][nj] == 0 and h_map[ni][nj] == 1:
                cnt += dfs(ni,nj)
                #return cnt -> 이건 끊기지 않고 한번에 연결하는 방법 찾기임
    return cnt


def solution():
    global N
    N = int(input())
    for i in range(N):
        h_map.append(list(map(int, list(input()))))
        visited.append([0 for _ in range(N)])

    result = []
    for i in range(N):
        for j in range(N):
            if h_map[i][j] == 1 and visited[i][j] == 0:
                result.append(dfs(i,j))

    print(len(result))
    for i in sorted(result): print(i)
    return
