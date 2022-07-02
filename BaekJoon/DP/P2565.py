"""
BaekJoon P2565 "전깃줄[LIS]" (DP[LIS] | Gold5)

[실수]

[부족한 점]
접근은 잘 했지만, 핵심적인 부분에 대해 생각하지 못함 -> LIS
DP로 분류되어 있지 않았다면 DP로 풀생각을 전혀 하지 못했을 것 같은 느낌
DP는 항상 더 많이 풀어보고 경험을 쌓자

[풀이]
LIS(최장 증가 수열)! -> 최고로 교차되지 않는 상황 구하기! (제거한다 생각하기 보다는)
모든 전깃줄의 정보를 A를 기준으로 오름차순 정렬 실시
1	8
2	2
3	9
4	1
6	4
7	6
9	7
10	10
정렬 후 이런 모습을 가지게 됨.
이제 여기서 A에 대해 B의 반복을 A의 인덱스 이전까지 진행하면서
지금 포커싱된 A의 B의 값보다 작은놈에 대해 판단 진행 -> 크면 교차! (A와B 모두 보다 작아야지 교차하지 않음)
    -> 최대값 판단 (현재 DP값 선택): 지금 고려된 애들 중에서 가장 큰값을 가지는애를 선택하고 거기다 1을 추가하면 됨
                                => dp[i] = max(dp[i], dp[j]+1) -> 현재 DP값 = max(이전에 고려된 것이 반영된 현재 dp값, 지금 새로 적용되는 dp값)
                                    => 최장 증가 수열
    그 후 가장 큰 DP값을 통해 결과를 산출하면 됨
% DP 값 : 인제 인덱스를 마지막 수열로 가질 수 있는 최장 증가 수열의 최대값
"""
import sys


def solution(n,li):
    li = sorted(li)
    dp = [1 for _ in range(n)] # 최장 증가 수열 값 저장
    for i in range(n):
        curr_b = li[i][1]
        # curr_max = dp[0]
        for j in range(i): # i 이전까지 반복 진행
            if li[j][1] < curr_b:
                # curr_max = max(curr_max, dp[j])
                # dp[i] = curr_max + 1
                dp[i] = max(dp[i], dp[j]+1) # 이전에 고려된 것이 반영된 현재 dp값, 지금 새로 적용되는 dp값 비교

    return n-max(dp)

if __name__ == '__main__':
    n = int(input())
    li = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    print(solution(n,li))
