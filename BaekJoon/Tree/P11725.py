# BaekJoon P11725 "트리의 부모 찾기" (트리, 그래프, DFS/BFS | S2)
"""
---[실수]---
---[부족한 점]---
---[풀이]---
양방향 그래프를 만들어주고,
지정된 루트를 따라 leaf node 까지 bfs/dfs 로 가주면서
현재 부모 노드와 자식 노드의 정보를 저장 -> parent_info
---[비고]---
LG CODE MONSTER 4번도 이런식으로 풀었으면 됐을 듯?
풀이시간: 13m
메모리: 81884 | 시간: 524
"""
import sys
from collections import defaultdict, deque


def find_parent(root, tree_info, n):
    parent_info = {}
    visited = [0 for _ in range(n)]
    visited[root] = 1
    q = deque([root])
    while q:
        curr_node = q.popleft()
        for next_node in tree_info[curr_node]:
            if not visited[next_node]:
                visited[next_node] = 1
                parent_info[next_node] = curr_node
                q.append(next_node)

    return parent_info


def solution(n, edges):
    tree_info = defaultdict(list)
    for edge in edges:
        a, b = edge[0] - 1, edge[1] - 1
        tree_info[a].append(b)
        tree_info[b].append(a)

    return find_parent(0, tree_info, n)


if __name__ == '__main__':
    N = int(input())
    inputs = [[*map(int, sys.stdin.readline().split())] for _ in range(N - 1)]
    answer = solution(N, inputs)
    for _, p in sorted(answer.items()):
        print(p + 1)
