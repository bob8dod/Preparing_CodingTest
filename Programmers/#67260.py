# 2020카카오 인턴십 _ more than 90min
"""
결론적으로 효율성 마지막 문제를 해결하지 못함. (재귀로 풀었기 때문이라 생각)
먼저 그래프를 생성해주고 (BFS를 통해)
그 그래프에 대해서 DFS를 통해 serach해줌
이때, 내가 들른 노드가 leaf 노드인지를 체크하며
해당 노드 밑으로 갈 필요가 없는지를 반복해서 체크 -> 이걸 leaf노드라고 설정
한 DFS가 끝날 때마다, 모든 노드를 찾았는지, 찾지 못했다면 leaf노드에 변화가 있는지를 확인하여
True False 판단
"""

from collections import deque, defaultdict
new_graph = defaultdict(list)

def make_graph(path):
    graph = defaultdict(list)
    for i in path:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    parents = deque([0])
    visited = {}
    while parents:
        tem = parents.popleft()
        visited[tem] = True
        for i in graph[tem]:
            if i not in visited:
                new_graph[tem].append(i)
                parents.append(i)
    return

dict_order = {}
stop = {}
leaf = {}

def dfs(i):
    if i in dict_order:
        del stop[dict_order[i]]
        del dict_order[i]

    if len(new_graph[i]) == 0:
        leaf[i] = 1
        return

    for j in new_graph[i]:
        if j not in stop and j not in leaf:
            dfs(j)

    cnt = 0
    for j in new_graph[i]:
        if j in leaf: cnt+=1

    if len(new_graph[i]) == cnt:
        leaf[i] = 1


def solution(n, path, order):
    make_graph(path)
    for i in range(n):
        if i in new_graph: continue
        new_graph[i] = []
    for i in order:
        dict_order[i[0]] = i[1]
        stop[i[1]] = True

    while True:
        before = leaf.copy()
        if 0 not in stop:
            dfs(0)
        if len(leaf) == n: return True
        if before == leaf: return False
