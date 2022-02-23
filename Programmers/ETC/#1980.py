# 프로그래머스 P1980 점프와 순간이동
"""
dp로 풀 순 있지만, 효율성에서 탈락됨.
앞에서 뒤로 가는 것이 아닌
도착지점에서 백트래킹하는 것으로 생각해보고
dp가 아닌 백트래킹에서의 수식으로 계산.
"""
def solution(n):
    # while n%2 == 0 : n/=2
    # n = int(n)
    # dp = [i for i in range(n+1)]
    # for i in range(2,n+1):
    #     if i%2 == 0: dp[i] = min(dp[i-1]+1, dp[i//2])
    #     else: dp[i] = dp[i-1] + 1
    #
    # return dp[n]
    cnt = 0
    while n != 1:
        if n%2 == 0: n = n//2
        else:
            n = n//2
            cnt+=1
    return cnt+1
