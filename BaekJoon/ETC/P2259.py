# BaekJoon P2259 "수열" (투 포인터, 윈도우 | S3)
"""
---[실수]---
---[부족한 점]---
---[풀이]---
---[비고]---
풀이 시간 : 15분
"""
import sys

# 시간초과 고려 X
def solution_before(n, k,nums):
    answer = -float('inf')
    for window in zip(*[nums[i:] for i in range(k)]):
        answer = max(answer, sum(window))

def solution(n, k,nums):
    answer = temp = sum(nums[:k])
    for plus in range(k,n):
        minus = plus - k
        temp -= nums[minus]
        temp += nums[plus]
        answer = max(answer, temp)

    return answer

if __name__ == '__main__':
    N, K = map(int, input().split())
    inputs = [*map(int, sys.stdin.readline().split())]
    print(solution(N,K,inputs))
