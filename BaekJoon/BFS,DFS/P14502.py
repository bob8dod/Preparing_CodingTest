# BaekJoon P14502 연구소 (구현+DFS/BFS,Gold5)
"""
[실수]
- deepcopy를 사용하여 2차원 배열을 복사하려함 -> deepcopy가 일반 for문으로 배정하는 것보다 100배 느림!

[부족했던 점]
- 구현이 너무 느림. 코드 작성만 20분 걸린듯!

[풀이]
일단 벽이 세워질 수 있는 위치에 대한 탐색을 combination으로 뽑아오고 판단하여 진행
3개 모두 벽이 세워질 수 있는 공간이다 -> 해당 벽들을 반영한 MAP에 대해 바이러스를 퍼트리는 bfs 진행
바이러스가 모두 퍼지고 난 후의 안전구역 count!
매 comination 마다의 결과의 count의 최댓값을 계속해서 비교 => answer

"""
from itertools import combinations
from collections import deque

di = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def bfs(temp, n, m):
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                q = deque([[i, j]])
                visited[i][j] = 1
                while q:
                    ci, cj = q.popleft()
                    for ti, tj in di:
                        ni, nj = ci + ti, cj + tj
                        if (0 <= ni < n and 0 <= nj < m) and not visited[ni][nj]:
                            visited[ni][nj] = 1
                            if temp[ni][nj] == 0:
                                temp[ni][nj] = 2
                                q.append([ni, nj])


def solution(n, m, gmap):
    num_list = [i for i in range(n * m)]
    answer = 0
    for com in combinations(num_list, 3):
        temp = [[i for i in row] for row in gmap]
        flag = 0

        for point in com:
            i, j = point // m, point % m
            if temp[i][j] != 0:
                flag = 1
                break
            else:
                temp[i][j] = 1

        if flag: continue

        bfs(temp, n, m)

        cnt = 0
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 0:
                    cnt += 1

        answer = max(answer, cnt)

    return answer


if __name__ == '__main__':
    N, M = map(int, input().split())
    gmap = [list(map(int, input().split())) for _ in range(N)]
    print(solution(N, M, gmap))
