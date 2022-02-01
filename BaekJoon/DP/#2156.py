# 2156 포도주 시식
"""
DP를 사용하는 문제.
일단 먼저 기본적으로 dp의 2인덱스까지는 범위문제 및 계산 때문에 따로 저장.
그 후 본격적으로 dp에 저장 시작.
이때 중요한 것은 3개씩 담는 윈도우가 있다고 생각하면서 풀어야됨
즉, 인덱스를 기준으로 자기자신, 직전, 2번째 전 을 계속해서 고려하면서 계산이 필요
저장 시 3가지의 경우를 비교하여 저장
1. 현재 인덱스를 포함하지 않는 경우 -> dp[i-1]
    즉 자신을 포함하지 않을 경우로 바로 직전까지 계산하여 최대값을 저장한 dp
2. 현재 인덱스와 2번째 전 인덱스를 포함 -> dp[i-2] + wine[i]
    즉 직전을 고르지 않고 2번째 전 의 dp를 포함. 이때, 꼭 dp로 계산해야됨
3. 현재 인덱스와 직전의 인덱스를 포함 -> dp[i-3] + wine[i-1] + wine[i]
    여기서 중요한 것은 내가 만약 2와 같이 dp[i-1] + wine[i] 로
    계산한다면 그 이전의 인덱스들이 어떻게 구성되는지 모르기에 규칙을 위반하게 됨
    그렇기에 규칙을 지키면서 최대값을 고려해야됨.
"""

import sys

N = int(input())
wine = [0 for _ in range(10000)]
dp = [0 for _ in range(10000)]
def solution(n):
    for i in range(N):
        wine[i] = int(sys.stdin.readline().strip())
    dp[0] = wine[0]
    dp[1] = dp[0] + wine[1]
    dp[2] = max(dp[1],dp[0]+wine[2],wine[1]+wine[2])
    for i in range(3,n):
        dp[i] = max(dp[i-1], dp[i-2] + wine[i], dp[i-3]+wine[i-1]+wine[i])

    return max(dp)

print(solution(N))
