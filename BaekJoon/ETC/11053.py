# BaekJoon P11053 "가장 긴 증가하는 부분수열" (DP | S2)
"""
---[실수]---
---[부족한 점]---
---[풀이]---
---[비고]---
"""
import sys
input = sys.stdin.readline

def solution(n, nums):
    memo = [1 for _ in range(n)]
    for i in range(1,n):
        prev, curr = nums[i-1], nums[i]
        if prev < curr:
            memo[i] = memo[i] + memo[i-1]
        else:
            memo[i] = memo[i-1]
    return max(memo)

if __name__ == '__main__':
    N = int(input())
    inputs = [*map(int, input().split())]
    print(solution(N, inputs))
