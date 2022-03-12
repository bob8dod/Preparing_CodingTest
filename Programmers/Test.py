def solution(width, height, diagonals):
    answer = 0
    for x,y in diagonals:
        dp = [[0 for _ in range(width + 1)] for _ in range(height + 1)]
        for i in range(height+1):
            for j in range(width+1):
                if i==0 and j==0:
                    dp[i][j] = 1
                    continue

                if i > x and j < y-1 :
                    continue
                elif i < x-1 and j > y : continue

                left, up = 0, 0
                if 0 <= j - 1 < width + 1: left = dp[i][j - 1]
                if 0 <= i - 1 < height + 1: up = dp[i - 1][j]
                dp[i][j] = left + up
                if i == x-1 and j==y:
                    dp[i][j] += dp[i+1][j-1]
                elif i == x and j==y-1:
                    dp[i][j] += dp[i-1][j+1]
                    # dp[x-1][y] = dp[i][j]
        print(dp)
        answer+= dp[-1][-1]
    print(answer)
