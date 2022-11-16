# BaekJoon P10971 "외판원순회2" (전수조사, 백트래킹 | S2)
"""
---[실수]---
---[부족한 점]---
백트래킹에서 global 을 사용하지 않는 풀이에서 아직 더딤
---[풀이]---
모든점에 대해 시작점으로 설정해주고
시작점에서 시작한 트래킹에서 모든 애들을 visit 하고 마지막 지점이 start 로 다시 돌아올 수 있는지 판단
다시 돌아올 수 있는 놈이면 최소 cost 에 반영
*중요* -> 애초에 최소 cost 보다 total cost 가 큰 경우에 대해서 고려할 필요가 없음 => 끊어줌
최소 cost 를 계속 반환해 주어 모든 백트래킹 지점에서 최소 cost 가 반영될 수 있도록 설정
---[비고]---
최적화 과정에서 세강이 코드를 많이 참고
풀이시간: 20m
메모리: 32440 | 시간: 228
"""
import sys
from collections import defaultdict


def dfs(start, curr_loc, info, visited, min_cost, total_cost,cnt,n, graph):

    if cnt == n and graph[curr_loc][start]:
        return min(min_cost, total_cost+graph[curr_loc][start])

    if total_cost > min_cost:
        return min_cost

    for next_loc, cost in info[curr_loc]:
        if not visited[next_loc]:
            visited[next_loc] = 1
            min_cost = dfs(start, next_loc, info, visited, min_cost, total_cost + cost, cnt+1, n, graph)
            visited[next_loc] = 0

    return min_cost


def solution(n, graph):
    info = defaultdict(list)
    for i in range(n):
        for j in range(n):
            cost = graph[i][j]
            if cost == 0: continue
            info[i].append([j,cost])


    answer = float('inf')
    visited = [0 for _ in range(n)]
    for start in range(n):
        visited[start] = 1
        answer = dfs(start, start, info, visited, answer, 0, 1, n, graph)
        visited[start] = 0

    return answer

if __name__ == '__main__':
    N = int(input())
    inputs = [[*map(int, sys.stdin.readline().split())] for _ in range(N)]
    print(solution(N, inputs))
