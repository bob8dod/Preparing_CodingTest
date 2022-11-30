# BaekJoon P2467 
"""
---[실수]---
---[부족한 점]---
어렵다..! 생각해내기가 너무 어려워~
---[풀이]---
핵심은 0보다 값이 크면 값을 줄여야 되므로 큰 값에 focus 되어 있는 end 를 줄여주고
      0보다 값이 작으면 값을 키워야 되므로 작은 값에 focus 되어 있는 start 를 줄여주면서
각 시점마다의 abs의 최소값을 기록하는 것
즉, 계속해서 격차를 줄여 0에 가깝게 만드는 것
---[비고]---
풀이 시간: 1h (1시간 넘도록 아이디어가 떠오르지 않아, 힌트 참고)
메모리: 42312 시간: 128
"""
import sys
input = sys.stdin.readline

def solution(n, nums):
    s, e = 0, n-1
    answer = abs(nums[s] + nums[e])
    left, right = nums[s], nums[e]
    while s < e:
        val = nums[s] + nums[e]
        check = abs(val)
        if check < answer:
            answer = check
            left, right = nums[s], nums[e]
        if val <= 0:
            s += 1
        else:
            e -= 1

    return left, right

if __name__ == '__main__':
    N = int(input().strip())
    inputs = [*map(int,input().split())]
    print(*solution(N,inputs))
