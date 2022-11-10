# BaekJoon P1987 "알파벳" (그래프, DFS/BFS | G4)
"""
---[실수]---
---[부족한 점]---
풀이 및 힌트를 참조하여 풀었음
---[풀이]---
bfs
queue 는 deque 가 아닌 set 으로 중복된 경로를 가진 놈들을 제거
다음 노드들 중 거쳐오지 않은 알파벳에 대해서만 넘어감 (문자열 in 을 이용하여 지나온 경로 판단)
현재 거처온 경로를 queue 에 같이 저장
---[비고]---
이상하지만, 한번쯤은 해보면 나쁘지 않은 문제인 듯
"""
import sys
# from collections import defaultdict, deque


# 시간 초과 -> dfs로 풀 수 있는 방법이 없음
def dfs(curr, graph, visited, d, r, c, curr_cnt, max_cnt):
    ci, cj = curr
    flag = 0
    for di, dj in d:
        ni, nj = ci + di, cj + dj
        if (0 <= ni < r and 0 <= nj < c) and not visited[graph[ni][nj]]:
            flag = 1
            visited[graph[ni][nj]] = 1
            max_cnt = dfs((ni, nj), graph, visited, d, r, c, curr_cnt + 1, max_cnt)
            visited[graph[ni][nj]] = 0

    if not flag:
        max_cnt = max(max_cnt, curr_cnt)

    return max_cnt


def bfs(start, graph, r, c):
    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    si, sj = start
    q = {(si, sj, graph[si][sj])} # set 을 통해 중복된 경로를 가진 놈들을 제거
    answer = 0  # or 1
    while q:
        ci, cj, visited = q.pop() # pop 해도 bfs 형식으로 돌아가는 가?
        answer = max(answer, len(visited))
        for di, dj in d:
            ni, nj = ci + di, cj + dj
            if (0 <= ni < r and 0 <= nj < c) and graph[ni][nj] not in visited: # 문자열 in 으로 경로 파악
                # or answer = max(answer, len(visited)+1)
                q.add((ni, nj, visited + graph[ni][nj]))

    return answer


def solution(r, c, graph):
    # d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    # visited = defaultdict(int)
    # visited[graph[0][0]] = 1
    # return dfs((0, 0), graph, visited, d, r, c, 1, 0)
    return bfs((0, 0), graph, r, c)


if __name__ == '__main__':
    R, C = map(int, input().split())
    inputs = [list(sys.stdin.readline().strip()) for _ in range(R)]
    print(solution(R, C, inputs))
