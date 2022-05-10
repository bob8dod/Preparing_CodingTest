# 백준 DP P12865 평범한 배낭 (Gold5)
"""
알고리즘:
- DP
- 0-1 배낭문제(0-1Knapsack Problem) : 담을 수 있는 물건이 나누어 질 수 없을 때(담는다 or 안담는다)
나의 실수:
- 단순한 DP문제라고 생각해서 1차원 DP로 해결하려 했음
- 하지만 이렇게 되면 현재 한계에서의 최대 가치를 알 수 있지만 어떤 물건이 담겨진지는 알 수가 없음
- 즉, 2차원으로 무게의 한계, 어떤 물건이 들어가는지 두가지 모두를 고려할 수 있어야 함!
풀이:
- dp 값 설정 부분 (항상 2차원적으로 생각해야 됨)
 1. 현재 물건(i)이 현재 가방(j)에 들어갈 수 있는지 판단
    1-1. 가능 (i <= j)
        - 현재 무게(j)에서 현재 물건을 고려하지 않았을 때(i-1)의 최대 가치 (dp[i-1][j]) 와
        - 현재 무게를 고려한 상태(무조건 포함)에서의 최대 가치 중
            - 현재 물건의 가치 (v) +
            - 전체 가방 무게에서 현재 물건을 뺀 무게(j-w)에서 현재 물건을 제외(i-1)한 최대 가치 (dp[i-1][j-w])
        => dp[i][j] = max(dp[i-1][j] , v + dp[i-1][j-w])
    1-2. 불가능 (i > j)
        - 그럼 현재 무게(j)에서 현재 물건을 제외한 이전 물건(i-1)들을 고려한 최대 가치를 이어 받아주면 됨
        => dp[i][j] = dp[i-1][j]
"""

import sys

def solution(N,K,info):
    dp = [[0 for _ in range(K+1)] for _ in range(N)]

    for j in range(K+1):
        w,v = info[0]
        if w <= j: dp[0][j] = v

    for i in range(1,N):
        w,v = info[i]
        for j in range(K+1):
            # 현재 물건이 최대 가방 무게보다 적을 때 -> 즉, 넣을 수 있는 상황
            if w <= j:
                # 현재 상태의 최대값 = 현재 물건을 고려하지 않은 상태의 최대값, 현재 물건을 고려한 상태의 최대값
                dp[i][j] = max(dp[i-1][j], v + dp[i-1][j-w])
            # 현재 물건이 최대 가방 무게보다 클 때 -> 즉, 넣을 수 없는 상황
            else:
                # 현재 상태의 최대값 = 현재 물건을 고려하지 않은 상태의 최대값
                dp[i][j] = dp[i-1][j]
    return dp[N-1][K]

if __name__ == '__main__':
    N, K = map(int,sys.stdin.readline().split())
    info = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    print(solution(N, K, info))
