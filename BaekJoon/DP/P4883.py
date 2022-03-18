# 백준 DP P4883 삼각 그래프
import sys
"""
각 노드의 값이 음수일 수 있기에 모든 경로를 탐색해 줘야 함 -> 인지 못해서 오래걸림
현재 노드로 올 수 있는 이전 노드에 대한 DP값 중 작은 값을 현재 DP값으로 UPDATE
"""
def main(N):
    gmap = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    dp = [gmap[0].copy()]+[[0,0,0] for _ in range(N-1)]

    # 0번째 줄
    dp[0][2] = gmap[0][2] + dp[0][1]

    # 1번째 줄
    dp[1][0] = gmap[1][0] + dp[0][1]
    dp[1][1] = gmap[1][1] + min(dp[1][0],dp[0][1], dp[0][2])
    dp[1][2] = gmap[1][2] + min(dp[1][1],dp[0][1],dp[0][2])

    # 2 ~ N-1 번째 줄
    for i in range(2,N):
        dp[i][0] = gmap[i][0] + min(dp[i-1][0],dp[i-1][1])
        dp[i][1] = gmap[i][1] + min(dp[i][0], dp[i-1][0], dp[i-1][1],dp[i-1][2])
        dp[i][2] = gmap[i][2] + min(dp[i][1],dp[i-1][1],dp[i-1][2])

    # 결과
    print("%d. %d" %(k, dp[-1][1]))

if __name__ == '__main__':
    k = 1
    while True:
        N = int(sys.stdin.readline().strip())
        if N == 0: break
        main(N)
        k+=1
