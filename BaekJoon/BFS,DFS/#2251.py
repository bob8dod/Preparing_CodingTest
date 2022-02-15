# 2251 물통
"""
물을 옮기는 모든 경우(6가지)에 대하여 뿌리를 내려줘야 함 -> DFS/BFS
이때, 물을 옮길 수 있는지 없는지 if문으로 판단하는 것이 아닌
수식을 통해 해결 -> ex) water = min(a, B-b) # A -> B
이는 물을 옮긴다고 가정했을 때 옮겨지는 물의 양을 정하는 수식.
즉, 내가 옮길 물통이 수용가능한 물의 양(B-b)과 물을 뺄 물통의 남아 있는 양(a) 중 작은 양으로 설정
"""
result = []

def dfs(a,b,c):

    if visited[a][b]:
        return

    visited[a][b] = 1
    if a == 0:
        result.append(c)

    # A -> B
    water = min(a, B-b)
    dfs(a-water, b+water, c)
    # A -> C
    water = min(a, C - c)
    dfs(a - water, b, c+water)
    # B -> A
    water = min(b, A - a)
    dfs(a + water, b - water, c)
    # B -> C
    water = min(b, C - c)
    dfs(a, b - water, c + water)
    # C -> A
    water = min(c, A- a)
    dfs(a + water, b, c - water)
    # C -> B
    water = min(c, B - b)
    dfs(a, b + water, c - water)



def solution(a,b,c):
    global A,B,C,visited
    A, B, C = a, b, c
    visited = [[0 for _ in range(b+1)] for _ in range(a+1)]
    dfs(0,0,c)
    for i in sorted(result):
        print(i, end=' ')

a, b, c = map(int,input().split())
solution(a,b,c)
