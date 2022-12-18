import sys
input = sys.stdin.readline


# 가장 기반이되는(작은) 부모 찾기
def find_parent(parents, curr):
    if parents[curr] != curr:
        parents[curr] = find_parent(parents, parents[curr])

    return parents[curr]

# 부모 통일화 (작은 쪽으로)
def union_parent(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b

def solution(v,e,edges):
    sorted_edges = sorted(edges, key=lambda x:x[2])
    parents = [i for i in range(v)]
    total = 0
    for at, bt, cost in sorted_edges:
        a, b = at - 1, bt - 1
        if find_parent(parents, a) != find_parent(parents, b): # NO Cycle
            union_parent(parents, a, b)
            total += cost

    return total

if __name__ == '__main__':
    V, E = map(int, input().split())
    inputs = [[*map(int, input().split())] for _ in range(E)]
    print(solution(V,E,inputs))
