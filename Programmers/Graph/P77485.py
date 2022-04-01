# 2021 Dev-Matching P77485 행렬 테두리 회전

from collections import deque

d = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def bfs(gmap, query, val):
    si, sj, ei, ej = query
    Q = deque([[si - 1, sj - 1, 0, 0]])
    min_value = val

    while Q:
        curr_i, curr_j, prev, di = Q.popleft()
        if di == 4:
            gmap[curr_i][curr_j] = prev
            return gmap, min_value

        ni, nj = curr_i + d[di][0], curr_j + d[di][1]
        if not (si - 1 <= ni <= ei - 1 and sj - 1 <= nj <= ej - 1):
            di += 1
            Q.append([curr_i, curr_j, prev, di])
        else:
            temp = gmap[curr_i][curr_j]
            if temp < min_value: min_value = temp
            gmap[curr_i][curr_j] = prev
            prev = temp
            Q.append([ni, nj, prev, di])


def solution(rows, columns, queries):
    gmap = [[0 for _ in range(columns)] for _ in range(rows)]
    val = 1
    for i in range(rows):
        for j in range(columns):
            gmap[i][j] = val
            val += 1

    result = []
    for query in queries:
        gmap, min_val = bfs(gmap, query, val)
        result.append(min_val)

    return result
