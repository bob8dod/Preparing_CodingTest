# BaekJoon P15685 "드래곤커브" ( 구현, 시뮬레이션 | G4)
"""
---[실수]---
x, y 인덱스 착각
---[부족한 점]---
---[풀이]---
앞선 경로들을 반대로 기억하며 -> appendleft
해당 경로들에 대해 -90도(idx+1)를 하면서 앞으로 나아가면 됨
---[비고]---
풀이시간: 1h
x, y 인덱스 착각해서 30m 날림
메모리: 32492 | 시간: 96
"""
import sys
from collections import deque


def make_curve(dragon, graph):
    direction = [[0, 1], [-1, 0], [0, -1], [1, 0]]
    x, y, d, g = dragon

    # default setting (0th generation)
    graph[y][x] = 1
    dir_y, dir_x = direction[d]
    y, x = y + dir_y, x + dir_x
    graph[y][x] = 1
    road = deque([d])

    for step in range(g):
        temp_road = [i for i in road]
        for ori_d in temp_road:
            next_d = (ori_d + 1) % 4
            dir_y, dir_x = direction[next_d]
            y, x = y + dir_y, x + dir_x
            graph[y][x] = 1
            road.appendleft(next_d)


def check_square(y, x, graph):
    cnt = 1
    to_check = [[1, 0], [1, 1], [0, 1]]
    for ty, tx in to_check:
        ny, nx = y + ty, x + tx
        if 0 <= nx <= 100 and 0 <= ny <= 100:
            cnt += graph[ny][nx]

    return cnt // 4


def solution(n, infos):
    graph = [[0 for _ in range(101)] for _ in range(101)]
    for dragon in infos:
        make_curve(dragon, graph)

    answer = 0
    for i in range(101):
        for j in range(101):
            if graph[i][j] == 1:
                answer += check_square(i, j, graph)

    return answer


if __name__ == '__main__':
    N = int(input())
    inputs = [[*map(int, sys.stdin.readline().split())] for _ in range(N)]
    print(solution(N, inputs))
