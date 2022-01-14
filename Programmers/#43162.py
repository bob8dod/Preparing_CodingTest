#네트워크 _ 28min
"""
BFS로 품.
기본적으로 모든 노드를 훑으면서
해당 노드가 방문되지 않은 노드일 경우에만 BFS 가동.

그래프 저장 시 양방향으로 그래프를 저장함.
그래서 추후에 이에 대해서 처리가 필요했음
이걸 dfs에서 visited로 판별함
-> 쨋든 반복문의 시작노드가 아닌 상태의
현재 탐색 중인 노드는 그 위의 상위 parent노드가 있음.
하지만 현재의 노드는 양방향으로 설정되었기 때문에
이 노드에 연결된 노드를 search하면 방금 타고 내려왔던 그 parent노드도 검출됨 -> 양방향으로 저장했기에
그래서 이걸 visited로 parent를 걸러줌.(parent는 당연히 visited이므로)
"""

from collections import defaultdict, deque
map_cp = defaultdict(list)
visited = {}

def bfs(i):
    Q = deque([i])
    while Q:
        curr = Q.popleft()
        for next in map_cp[curr]:
            if next not in visited: # [중요!] _ 자신의 부모를 제거하기 위해
                visited[next] = True
                Q.append(next)

    return 1


def solution(n, computers):
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1: map_cp[i].append(j)

    cnt = 0
    for i in range(n):
        if i not in visited:
            visited[i] = True
            cnt += bfs(i)
    return cnt
