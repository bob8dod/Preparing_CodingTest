# 숨바꼭질 _ 잘못된 풀이
"""
BFS 복습 없이 풀었을 때
DP로 잘못 접근.
"""
import sys

memo = {}
def check(n,k):
    if n == k: return 0
    memo[n] = True
    sub = [n-1, n+1, n*2]
    print(sub)
    ch = []
    for i in sub:
        if 0 <= i <= k+1 and i not in memo:
            ch.append(check(i,k))

    if len(ch)==0: return sys.maxsize
    tem = 1 + min(ch)
    memo[n] = tem
    return tem

def solution():
    N, K = map(int, input().split())
    return check(N,K)

print(solution())
