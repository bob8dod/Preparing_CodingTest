# 숨바꼭질 최적화 _ using DP(재귀)
"""
정석적인 풀이는 아님. 이 문제를 완벽히 파악하고 그 핵심을 짚어야지만 구현 가능
n이 아닌 k가 움직인다고 생각.
n이 k와 같으면 종료, n이 k보다 크다면 사실 그냥 뒤로 움직이는 방법 밖에 없기에 n-k
이제 이 풀이의 핵심 부분
만약 k가 2로 나누어진다면 2로 나누거나 계속 1씩 이동하는 것 중 최솟값을 판단. (2로 나누어진다고 무조건 나누면 안됨)
나누어지지 않는다면 -1, +1로 이동했을 때의 최솟값을 비교.
"""

def find(n,k):
    # end point
    if n == k: return 0
    if n > k: return n-k
    # ing poin
    if k%2==0: return min(k-n, find(n,k//2)+1)
    else: return min(find(n,k-1),find(n,k+1)) + 1

def solution():
    N, K = map(int, input().split())
    return find(N,K)
