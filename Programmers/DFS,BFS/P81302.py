# P81302 거리두기 확인하기

"""
'P'에 해당하는 순간,
이 'P' 주위 2거리 안에 다른 'P'가 존재하는 지
BFS를 통해서 확인.
Queue를 통해 idx와 distance 정보를 통해 
거리와 해당 idx의 값을 확인하며 판단.
"""

from collections import deque

directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def bfs(i, j, gmap):
    visited = [[0 for _ in range(5)] for _ in range(5)]
    visited[i][j] = 1
    queue = deque([[i, j, 0]])
    while queue:
        ci, cj, dis = queue.popleft()

        if dis == 2: continue

        for di, dj in directions:
            ni, nj = ci + di, cj + dj
            if (0 <= ni < 5 and 0 <= nj < 5) and not visited[ni][nj] and gmap[ni][nj] != 'X':
                visited[ni][nj] = 1
                if gmap[ni][nj] == 'P':
                    return False
                queue.append([ni, nj, dis + 1])
    return True


def solution(places):
    answer = []
    for place in places:

        temp = 1

        gmap = []
        for p in place:
            gmap.append(list(p))

        for i in range(5):
            for j in range(5):
                if gmap[i][j] == 'P':
                    if not bfs(i, j, gmap):
                        temp = 0
                        break
            if temp == 0: break

        answer.append(temp)

    return answer
