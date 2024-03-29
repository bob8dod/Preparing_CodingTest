# BaekJoon P1912 "연속합" (DP | S2)
"""
---[실수]---
---[부족한 점]---
점화식을 생각해내는 능력 부족
한단계만을 거쳐서 풀려고 함 -> dp[-1]
두단계를 거쳐서 답을 낼 수도 있다는 생각 필요 -> max(dp)
---[풀이]---
dp -> 현재 값이 혼자있을 때 vs 이전 무리와 이어질 때
max(dp) -> 혼자있든 뭉쳐있든 그 무리 중에서 가장 큰 값

dp[i] = max(li[i], dp[i-1]+li[i])
=> 현재 저장할 값 = 혼자있을 때 vs 이전 무리와 이어질 때 중 큰 값 [무리 후보]
 -> 무리를 이어갈지 안이어갈지에 대한 판단
 max(dp) -> 그런 무리들 중에서 최대 값

주의점
dp[i] 는 현재값까지의 최대값 이 아닌
현재 값은 무조건 포함된 상태에서 혼자 있을 때 값과 이전 무리와 연속되어 무리를 지어있을 때의 값 중 큰 값
여기서 이전 무리와 연결되어있는지 어떻게 알지? 라고 생각할 수 있지만,
항상 이전무리는 현재의 바로 직전의 값을 포함하고 있기에 걱정할 필요가 없음

---[비고]---
"""
import sys


def solution(n, li):
    dp = [i for i in li]
    for i in range(1,n):
        dp[i] = max(li[i], dp[i-1]+li[i])

    return max(dp)

if __name__ == '__main__':
    N = int(input())
    li = list(map(int, sys.stdin.readline().split()))
    print(solution(N, li))
