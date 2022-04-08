# 프로그래머스 2020 카카오 인턴십 BFS+DP P67259 경주로 건설
"""
BFS를 통해서 0,0 에서 퍼져 가면서
현재 인덱스에서 갈 수 있는 다음 idx를 파악하고
그 다음 idx에 저장되어 있는 dp값보다 작은 경우,
값을 현재 값으로 변경하고, 그 다음 idx로 bfs 계속 진행
여기서 중요한 부분은 현재idx에서 다음idx로 넘어갈 때 드는 비용이
그 다음 idx의 현재 dp에 저장되어 있는 비용보다 작을 경우에만
Q에 append해주어서 BFS를 계속 진행해 나가는 것!
-> 이걸 통해 방향에 따른 최소경로를 처리할 수 있음.
-> 그 다음 idx를 토대로 또 BFS를 나가는 것이므로!

[잘못된 풀이]
처음엔 cnt랑 curve랑 dir을 dp로 저장했었음
하지만 dp는 수시로 바뀌기 때문에 그 당시의 각 변수들의 값을 유지할 수가 없음 당연히.
그러기 때문에 Q 자체에 cnt,curve,dir을 넣어야지 
그 당시의 해당 변수들의 값을 유지한 상태로 BFS를 진행할 수 있음!!
"""
import sys
from collections import deque

def solution(board):
    n = len(board)
    answer = sys.maxsize
    dp = [[sys.maxsize for _ in range(n)] for _ in range(n)]
    # 현재 지나간 길을 확인하기 위한 idx 추가
    directions = [(-1, 0, 0), (0, 1, 1), (1, 0, 2), (0, -1, 3)]
    # i, j, cost, direction
    q = deque([(0, 0, 0, -1)])
    while q:
        i, j, cost, dir_idx = q.popleft()
        # 정답 범위이고, 현재 cost가 더 적을 때 값 할당
        if (i, j) == (n - 1, n - 1) and answer > cost:
            answer = cost
        for direction in directions:
            # 다음 값 셋팅
            next_i = i + direction[0]
            next_j = j + direction[1]
            add_cost = 1 if dir_idx == direction[2] or dir_idx == -1 else 6
            # 현재 값 판단할 지 여부
            if not (0 <= next_i < n and 0 <= next_j < n) or board[next_i][next_j] == 1:
                continue
            if dp[next_i][next_j] < cost + add_cost - 4:
                continue
            # dp에 값 설정 및 큐에 추가
            dp[next_i][next_j] = cost + add_cost
            q.append((next_i, next_j, cost + add_cost, direction[2]))
    return answer * 100
