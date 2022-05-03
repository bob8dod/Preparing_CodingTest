# P7576 토마토
"""
그냥 일반적인 bfs를 사용하려 했지만, 실패.

즉 일반적인 bfs가 아닌,
매 순간에 접근하는 위치를 따로 저장해서
그 다음 순간에 그 위치들을 모은 list들만을 search 하여 시간복잡도를 줄임
"""

import sys

directions = [[0,1], [1,0], [0,-1],[-1,0]]

def bfs(start_queue,gmap):

    cnt = 0
    queue = start_queue.copy()
    visited = [[0 for _ in range(M)] for _ in range(N)]
    for i,j in queue:
        visited[i][j] = 1

    while True:
        next_queue = []
        for i,j in queue:
            for di,dj in directions:
                ni, nj = i + di, j + dj
                if (0<= ni < N and 0<= nj < M) and  not visited[ni][nj] and gmap[ni][nj] == 0:
                    visited[i][j] = 1
                    gmap[ni][nj] = 1
                    next_queue.append([ni,nj])
        if len(next_queue) == 0: return cnt
        cnt += 1
        queue = next_queue.copy()


def solution(N,M,gmap):

    start_queue = []
    flag = 0
    for i in range(N):
        for j in range(M):
            if gmap[i][j] == 1:
                start_queue.append([i,j])
            if gmap[i][j] == 0:
                flag = 1

    if flag == 0: return 0

    answer = bfs(start_queue,gmap)

    for i in range(N):
        for j in range(M):
            if gmap[i][j] == 0:
                answer = -1
                break

    return answer



if __name__ == '__main__':
    M, N = map(int, sys.stdin.readline().split())
    li = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

    print(solution(N, M, li))

