# 동굴탐험 BestCode
"""
핵심 개념은 내가 넘어가지 못하는 노드에 대해 접근했을때,
이 노드를 열어주는 연결 노드에 대해 기록하고 그 연결 노드에 visited했을 때, 바로 못넘었던 노드로 연결해주는 것
접근하지도 않았는데 연결 노드에 도착했다고 바로 막힌 노드로 넘어가게 되면 놓치는 노드가 있을 수 있음
그니깐 가장 중요한건 못가는 노드라고 아예 배제하는 것이 아닌 접근기록을 남기는 것
큐or스택에 넣어준 다음에 연결노드에 방문하면 바로 그 막힌 노드로 넘어가는 것
"""

from collections import deque

def bfs(i):
    q = deque([i])
    while q:
        curr = q.popleft()

        if orders[curr] and not visited[orders[curr]]:
            after[orders[curr]] = curr
            continue

        visited[curr] = True

        for next in tree[curr]:
            if not visited[next]:
                q.append(next)

        if curr in after:
            q.append(after[curr])

    return


def solution(n, path, order):
    # path 정보로 부터 인접 리스트를 구현한다.
    global tree, orders, visited, after
    tree = [[] for _ in range(n)]
    orders = [0 for i in range(n)]
    visited = [False for i in range(n)]
    after = {}

    for v1, v2 in path:
        tree[v1].append(v2)
        tree[v2].append(v1)

    for pre, post in order:
        orders[post] = pre

    bfs(0)

    return n == len(visited)
