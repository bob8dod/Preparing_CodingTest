# BaekJoon P9251 LCS (DP | Gold5)
"""
[부족한 점]
DP로 풀생각을 전혀 못함.
DP로 풀어야 겠다 했어도 못풀었을 듯.
DP를 1차원 뿐만 아니라 2차원에서의 상황도 고려해야 됨.
DP의 값을 설정하는 부분만 고려할 것이 아닌,
그 직전의 DP값 설정이 분기되는 과정도 고려할 필요가 있음

[풀이]
다이나믹 프로그래밍 (DP)
기본적으로 DP로 보면, 하나씩 문자가 이어붙어간다고 생각하고,
붙었을 때와 붙지 않았을 때의 상황을 비교하면 됨.
하지만 여기선 붙었을 때의 경우를 2차원적으로 봐야함.
즉, 현재 기준이 되는 row(i)와 col(j), 이 두가지 문자가 동시에 추가된다고 생각하면 됨.
이 때 추가가 될 때 2가지로 판단이 필요.
1. 지금 추가되는 두 문자가 동일한 문자 인가
    -> 다른 판단 필요 없이 지금 추가되는 두 문자가 없었던 상태의 LCS값(dp[i-1][j-1])에 +1을 추가
        ==> 동일한 문자가 추가되면 당연히 LCS값은 1이 추가됨
    `dp[i][j] = dp[i-1][j-1] + 1`
2. [중요] 지금 추가되는 두 문자가 동일하지 않은 문자
    -> row(i)만 추가된 상태(dp[i][j-1])의 LCS vs col(j)만 추가된 상태(dp[i-1][j])의 LCS 를 비교해서 큰 값 설정
    `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`
이렇게 되면 자동으로 dp[끝][끝] 에는 모든 문자열이 고려된 LCS값이 저장됨
"""

def solution(a,b):
    a, b = list(a), list(b)
    dp = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            if b[j-1] == a[i-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[len(a)][len(b)]


if __name__ == '__main__':
    a = input()
    b = input()
    print(solution(a,b))
