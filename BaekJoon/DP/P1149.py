# 백준 P1149 RGB [DP, Silver1]
"""
DP로 풀어야 겠다는 것은 알아차렸으나, 
지금까지 1차원 DP로만 풀어와서 2차원으로 풀어야겠다는 생각을 못함 -> 생각이 짧음
어쨌든 추가되는 집에 대해서 가능한 경우에 따른 DP를 점화식으로 표현해야되는데,
1차원으로는 절대 모든 경우를 고려할 수 없음.
2차원으로 각각의 선택에 따른 이전의 가능한 선택을 또 해야되기에 2차원으로 진행해야됨.
ex) 3번째 집의 dp값 -> 3번째 집을 R로 할때 -> 2번째 집은 B,G 중 최소값 |
 B로 할 때 -> 2번째 집은 R,G 중 최소값 | G로 할때 -> 2번째 집은 R,B 중 최소값 |
 이런 식으로 선택에 따른 또 다른 이전 선택이 필요하기에 2차원으로 풀어야됨.
"""
def main():
    N = int(input())
    gmap = [[0,0,0]] + [list(map(int,input().split())) for _ in range(N)]
    dp = [[0 for _ in range(3)] for _ in range(N+1)]
    dp[1] = gmap[1].copy()
    for i in range(1,N+1):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + gmap[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + gmap[i][1]
        dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + gmap[i][2]

    print(min(dp[N]))


if __name__ == "__main__":
    main()
