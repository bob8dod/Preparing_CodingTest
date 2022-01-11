from collections import deque, defaultdict
graph = defaultdict(list)
new_graph = defaultdict(dict)
visited = {}

def make_graph(path):
    for i in path:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    parents = deque([0])
    while parents:
        tem = parents.popleft()
        visited[tem] = True
        for i in graph[tem]:
            if i not in visited:
                new_graph[tem][i] = 1
                parents.append(i)
    return

dict_order = {}
stop = {}
visit = {}

def dfs(i):
    if i in dict_order:
        del stop[dict_order[i]]
        del dict_order[i]

    if len(new_graph[i]) == 0: return 1
    for j in new_graph[i]:
        if j not in stop:
            if dfs(j) == 1: del new_graph[i][j]



def solution(n, path, order):
    make_graph(path)
    for i in range(n):
        if i not in new_graph: new_graph[i]= {}
    for i in order:
        dict_order[i[0]] = i[1]
        stop[i[1]] = True
    for i in range(n): visit[i] = 0

    while new_graph:
        dfs(0)

    answer = dfs(0)
    return answer

make_graph([[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]])
print(new_graph)
