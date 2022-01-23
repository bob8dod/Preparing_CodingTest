#호텔
"""
내가 직접 짜 본 version
"""
import sys

C, N = map(int,input().split())
city = [list(map(int,input().split())) for _ in range(N)]
dp = [0]+[sys.maxsize for _ in range(C+99)]

def solution(N, C, city):
    for cost, person in city:
        for j in range(person, C+100):
            dp[j] = min(dp[j], dp[j-person]+cost)

    return min(dp[C:])

print(solution(N,C,city))
