# 백준 DFS/BFS P11403 경로 찾기
import sys
from collections import deque
"""
먼저 모든 노드들에 대한 간선 정보를 저장한 후
각 노드들에 대해 BFS를 진행하며 갈 수 있는 노드들에 대해 기록 진행.
"""

def bfs(info, i, N):
    global result
    Q = deque([i])
    visited = [0 for _ in range(N)]
    while Q:
        curr = Q.popleft()
        for next in info[curr]:
            if not visited[next]:
                visited[next] = 1
                result[i][next] = 1
                Q.append(next)


def main():
    global result
    N = int(sys.stdin.readline().strip())
    gmap = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    info = [[] for _ in range(N)]
    result = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if gmap[i][j] == 1:
                info[i].append(j)

    for i in range(N):
        bfs(info, i, N)

    for i in range(N):
        for j in range(N):
            print(result[i][j], end=' ')
        print()


if __name__ == "__main__":
    main()
