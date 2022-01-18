# 동굴 탐험 _ 직접 푼 버전
from collections import deque, defaultdict
"""
BFS로 푼 버전. (DFS 재귀로 풀면 시간초과)
가장 핵심적인 개념은 
'가지 못하는 노드'를 가기 위해 '해당 노드 전에 들려야하는 노드'를 들른 상태이냐 아니냐(visited)의 문제
1) 이미 들른 상태이다. -> 그냥 일반 노드 처리하듯이 처리해주면 됨
2) 들르지 않았다. -> 그 순간 후처리 진행
    ㄴ 후처리: '해당 노드 전에 들려야하는 노드'를 나중에 들르게 될 때, 해당 노드를 연결해줌
            즉, Queue에 저장해서 연결해준다는 것.
            이를 위해 해당 노드가 후처리가 필요하다는 표시를 jump_to를 통해 해줌
            그러면 '해당 노드 전에 들려야하는 노드'를 들르게 되면 jump_to를 통해 해당 노드로 점프해서 오게 됨
!! 즉, 가지 못하는 노드가 기준이됨. (order의 저장방식과는 다르게)
"""
def bfs(i):
    Q = deque([i])
    if i in dict_order: return
    while Q:
        curr = Q.popleft()
        visited[curr] = 1

        for next in cave[curr]:
            if next in dict_order and not visited[dict_order[next]]: # 가지 못하는 놈에 대한 처리 (후처리를 위한 작업)
                jump_to[dict_order[next]] = next
            elif not visited[next]: # 부모 노드를 제외하기 위함
                Q.append(next)

        if curr in jump_to: Q.append(jump_to[curr])

def solution(n, path, order):
    global cave, dict_order, visited, jump_to
    cave = defaultdict(list)
    dict_order = {i[1]:i[0] for i in order}
    jump_to = {}
    visited = [0 for _ in range(n)]

    for i in path:
        cave[i[0]].append(i[1])
        cave[i[1]].append(i[0])

    bfs(0)

    return True if sum(visited)==n else False
