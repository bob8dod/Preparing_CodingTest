# 백준 DP P2302 극장 좌석
def main():
    N = int(input())
    M = int(input())

    V = [0] + [int(input()) for _ in range(M)] +[N+1]

    dp = [1 for _ in range(N+1)]
    dp[1] = 1
    dp[2] = 2
    for i in range(3, N+1):
        dp[i] = dp[i-1] + dp[i-2]

    total = 1
    for i in range(len(V)-1):
        length = (V[i+1] - V[i] - 1)
        total *= dp[length]

    print(total)

if __name__ == "__main__":
    main()
