# 백준 DP P10844 쉬운 계단 수
"""
DP라 생각을 했지만, 또 1차원적으로만 생각함.
해당 문제를 보면, 각 dp에 0~9라는 경우의 수가 있고
그 경우의 수에 따른 최종 dp가 또 있음. 즉, 2차원으로 생각해서 점화식을 구성해야됨.
[풀이]
이 또한 다른 DP들 처럼 뒤에 숫자가 붙을 경우 해당 조건에 만족하는 지를 설정
예를 들어 3자리 수에 대한 판단이 이루어진다고 할 때,
[][] + [] 여기서 추가로 붙는 []에 0-9가 들어갈 수 있기에 이를 기준으로 점화식을 구성하면됨
만약 2가 들어간다면 2번째의 []에는 1이나 3이 들어갈 수 있음.
그럼 이제 2자리일 때의 1과 3일 때의 dp값을 가져와서 더해주면되는 것.
그럼 dp는 이런식으로 구성됨
  0 1 2 3 4 5 6 7 8 9
1 0 1 1 1 1 1 1 1 1 1
2 1 1 2 2 2 2 2 2 2 1
3
.
.
결국 점화식은 각 윗칸의 대각선의 합으로 만들 수 있음.
"""
def main():
    N = int(input())
    dp = [[0 for _ in range(10)] for _ in range(N)]
    result = [0 for _ in range(N)]

    dp[0] = [0,1,1,1,1,1,1,1,1,1]
    for i in range(N):
        if i != 0:
            dp[i][0] = dp[i-1][1]
            dp[i][9] = dp[i-1][8]
            for j in range(1,9):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        result[i] = sum(dp[i]) % 1000000000

    print(result[-1])



if __name__ == "__main__":
    main()