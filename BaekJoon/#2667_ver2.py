# 단지 번호 붙이기 _ 60min
"""
DFS로 푼 버전.
먼저 DFS가 한번이 아닌 여러 번 진행해야 하기 때문에 solution함수에서 반복문을 통해
모든 요소에 접근하도록 한 후 방문했는지, 1인지를 판단하여 DFS 진행, 그 결과를 result에 누적
DFS가 이루어지는 부분에서는 연결되어 더 나아가는 그 순간에서 1씩 더함.
즉, root에서 leaf로 나아가며 cnt를 인자로 보내줌으로써 더해짐
재귀적 측면에서 자식노드에서 부모노드로 가는 방향에서는 cnt를 인자로 보내줌으로써
현재까지 계산된 cnt를 공유해줌. 그 후 해당 cnt값을 가지고 계속해서 연산진행
! dfs로 들어오는 그 해당 노드를 자식노드가 아닌 부모노드로 봐야되는 것이 핵심!
"""
h_map = []
visited = []
di = [0,0,-1,1]
dj = [1,-1,0,0]


def dfs(i,j, cnt):
    cnt+=1
    visited[i][j]=1
    for tem_i,tem_j in zip(di,dj):
        ni, nj = i + tem_i, j + tem_j
        if 0<=ni<N and 0<=nj<N:
            if visited[ni][nj] == 0 and h_map[ni][nj] == 1:
                cnt = dfs(ni,nj, cnt)
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
                result.append(dfs(i, j, 0))

    print(len(result))
    for i in sorted(result): print(i)
    return

solution()
