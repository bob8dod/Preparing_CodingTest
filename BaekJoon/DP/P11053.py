# BaekJoon P11053 "가장 증가하는 부분 수열" (DP | S2)
"""
---[실수]---
---[부족한 점]---
DP 연습 필요
---[풀이]---
전체 요소를 차례대로 보면서
현재 지점까지 최대 증가 수열을 기록하는 것.
현재 지점까지 요소를 훑으면서, 현재 지점보다 해당 요소가 작으면
해당 요소의 memo 값(해당 요소까지의 최대 증가 수열의 길이)를 가져와 
지금까지 훑은 다른 요소들의 memo 값들과 비교하여 가장 긴 수열에 +1 을하여 현재 지점을 포함해주는 것
---[비고]---
"""
import sys
input = sys.stdin.readline

def solution(n, nums):
    memo = [1 for _ in range(n)]
    for i in range(n):
        curr = nums[i]
        for j in range(i):
            prev = nums[j]
            if prev < curr:
                memo[i] = max(memo[i], memo[j]+1)

    return max(memo)
if __name__ == '__main__':
    N = int(input())
    inputs = [*map(int, input().split())]
    print(solution(N, inputs))
