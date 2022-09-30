# BaekJoon P21608 "상어초등학교" (구현 | G5)
"""
---[실수]---
---[부족한 점]---
---[풀이]---
---[비고]---
"""
import sys


def sit_down(graph, n, curr, didi):
    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    candidates = []
    for ci in range(n):
        for cj in range(n):
            friends_cnt = 0
            empty_cnt = 0
            if not graph[ci][cj]:
                for di, dj in d:
                    ni, nj = ci + di, cj + dj
                    if 0 <= ni < n and 0 <= nj < n:
                        # 1번 조건 (주변 친구 개수)
                        if graph[ni][nj] in didi[curr]:
                            friends_cnt += 1
                        # 2번 조건 (주변 빈칸 개수)
                        if graph[ni][nj] == 0:
                            empty_cnt += 1
                candidates.append([-friends_cnt, -empty_cnt, ci, cj])
    _, _, i, j = min(candidates)
    return i,j


def solution(n, students):
    graph = [[0 for _ in range(n)] for _ in range(n)]
    didi = dict()
    for st in students:
        didi[st[0]] = set(st[1:])
        i, j = sit_down(graph, n, st[0], didi)
        graph[i][j] = st[0]

    total = 0
    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for ci in range(n):
        for cj in range(n):
            friends_cnt = 0
            for di, dj in d:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < n and 0 <= nj < n:
                    # 1번 조건 (주변 친구 개수)
                    if graph[ni][nj] in didi[graph[ci][cj]]:
                        friends_cnt += 1
            if friends_cnt != 0 : total += 10**(friends_cnt-1)

    return total

if __name__ == '__main__':
    N = int(input())
    inputs = [[*map(int, sys.stdin.readline().split())] for _ in range(N * N)]
    print(solution(N, inputs))
