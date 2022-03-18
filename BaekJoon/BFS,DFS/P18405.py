# 백준 DFS/BFS P18405 경쟁적 전염
"""
초를 기준으로 bfs를 실시.
bfs는 각 모든 바이러스가 있는 위치에서 4방향으로 한번씩 뻗어가는 형식.
여기서 중요한 것은 바이러스마다의 Q를 만들어서 각 바이러스에 맞는 bfs를 진행.
한 초마다 현재 남아 있는 Q를 모두 지우고 갈 수 있는 새로운 요소들을 Q에 저장.
"""
import sys
from collections import deque

def bfs():
    for idx in range(len(check)):
        tem_len = len(check[idx])
        for _ in range(tem_len):
            i,j = check[idx].popleft()
            for ti, tj in zip(di,dj):
                ni, nj = i+ti, j +tj
                if (0<= ni < N and 0<= nj <N) and not gmap[ni][nj]:
                    gmap[ni][nj] = idx
                    check[idx].append([ni,nj])

def main():
    for i in range(N):
        for j in range(N):
            if gmap[i][j]:
                check[gmap[i][j]].append([i,j])
    for _ in range(S):
        bfs()

if __name__ == "__main__":
    N, K = map(int, input().split())
    gmap = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    S, X, Y = map(int, input().split()) # x-1, y-1
    check = [deque() for _ in range(K + 1)]
    di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
    main()
    print(gmap[X-1][Y-1])
