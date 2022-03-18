# 백준 DP P10164 격자상의 경로
"""
sub함수가 처음에 작성한 코드.
sub함수의 전략은 필수로 들러야 하는 경로가 존재하다면, 그 경로를 선택하기 위해 
선택하면 안될 경로에 대해서 막아둔 다음에 DP를 계산했음.
하지만, 이는 복잡하기도 하고 문제 조건이 더 까다로워진다면, 사용하기 힘듦.
그래서 main으로 풀어야 됨.
main 함수의 전략은 기존의 초등학교때 배운 최단경로 루트.
즉, 내가 꼭 거쳐야될 지점까지의 경로 Dp를 구하고
다시 거쳐야될 지점부터 끝까지의 경로 DP를 구한다음
두 값을 곱해주는 전략 -> 까다로운 조건이 붙어도 간단히 해결 가능.
"""

"""
def sub():
    if K:
        ti = (K-1)//M
        tj = (K-1)%M
        if ti+1 < N:
            for j in range(tj):
                gmap[ti+1][j] = 1
        if ti-1 >=0:
            for j in range(tj+1,M):
                gmap[ti-1][j] = 1

    dp[1][1] = 1
    for i in range(1,N+1):
        for j in range(1,M+1):
            if i==1 and j==1 : continue
            if gmap[i-1][j-1] == 1: continue
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    print(dp[N][M])
"""

def main():
    ti, tj = 1, 1
    tem = 1
    if K:
        ti = (K-1)//M +1
        tj = (K-1)%M +1
        dp[1][1] = 1
        for i in range(1,ti+1):
            for j in range(1,tj+1):
                if i == 1 and j == 1: continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        tem = dp[ti][tj]

    dp[ti][tj] = 1
    for i in range(ti,N+1):
        for j in range(tj,M+1):
            if i == ti and j == tj: continue
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    print(tem*dp[N][M])


if __name__ == '__main__':
    N, M, K = map(int, input().split())
    dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    main()
