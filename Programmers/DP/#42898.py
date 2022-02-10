# 42898 등굣길 _ 60m
"""
DFS로 접근했다가 시간초과로 맨탈 아웃.
애초에 mod로 구하는 건 DP로 밖에 못함. 주의하도록.
항상 DFS, BFS 등 모든 접근하기 전에 DP로 풀 수 있을지 조금이라도 고민해보자.

[풀이]
문제에서 오른쪽과 아래로만 이동이 가능하다고 함.
즉, 현재 위치에서 올 수 있는 방향은 위, 왼쪽만 확인하면 됨. 즉, 최소 거리는 걍 위, 왼쪽에서 온 놈들임
그러면서 현재 위치가 도착지라고 생각하며 
그 지점까지 올 수 있는 최소거리(좌, 상에서 나온 개수)의 개수를 더해주면 됨 -> DP
# DP도 사실상 유형이 항상 비슷하다!!!!!! -> 어떻게 하면 바로 직전의 값을 이용할까, 어떻게 누적시킬까...
"""

def solution(m, n, puddles):
    mod = 1000000007
    dp = [[0 for _ in range(m)] for _ in range(n)]
    gmap = [[0 for _ in range(m)] for _ in range(n)]
    for puddle in puddles:
        gmap[puddle[1]-1][puddle[0]-1] = 1

    for i in range(n):
        if gmap[i][0] == 1:
            break;
        dp[i][0] = 1
    for j in range(m):
        if gmap[0][j] == 1:
            break
        dp[0][j] = 1

    for i in range(1,n):
        for j in range(1,m):
            if gmap[i][j] != 1:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1])%mod

    return dp[n-1][m-1]
