# 백준 DP P11660 구간 합 구하기 5
"""
그냥 모든 애들에 대해서 반복문으로 덧셈으로 진행하면 -> 시간초과
DP로 풀어내야 함!
[풀이]
먼저 각 index까지의 사각형의 합을 구해줌
이때 사각형은 현재 자기 자신, 왼쪽 범위 사각형, 위쪽 범위 사각형을 더하고 마지막으로 겹치는 부분을 빼주면 구할 수 있음.
이를 dp 점화식으로 표현하면 됨.
이때, 최자측, 최상단 놈들을 DP에 적용하기 위해서
0으로 채워준 상태로 dp를 만들어줌 -> dp의 크기가 n+1, n+1 인 이유

마지막으로 그 차를 구할때는 DP값들을 똑같이 이용해주면 됨
"""
import sys

def main():
    N, M = map(int, input().split())
    gmap = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,N+1):
            dp[i][j] = gmap[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

    for i in range(M):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        result = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
        sys.stdout.write(str(result) + "\n")



if __name__ == "__main__":
    main()
