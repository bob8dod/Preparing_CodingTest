#호텔 _ 80min
"""
DFS + DP로 푼 버전
기본적으로 밑에서 부터 반환하며 값을 합쳐서 memo에 저장하는데
이때 중요한건 해당 노드를 memo에 저장할때, 그 가지들이 반환하는 값 중 가장 최솟값으로 저장해야됨. 이게 핵심!!
여기서 dfs로 들어온 노드의 값이 해당 기준보다 커지면 그냥 0을 반환 (더이상 해주는게 없으므로)
아니면 들어온 노드가 이미 탐색이 완료된 즉, memo에 있는 값이면 그 해당 값 반환 (DP)
그 반환 값들을 밑에서 부터 반환하며 차근차근 더해주어 결론적인 0에 최솟값을 저장.
# 문제를 제대로 읽지않아 시간 10-15분 지연
# sys.setrecursionlimit(10000)을 몰라 10-15분 지연 -> recursion error 방지
"""
import sys
sys.setrecursionlimit(10000)

city = []
C, N = map(int, input().split())
for i in range(N):
    m, p = map(int, input().split())
    city.append([m, p])

memo = {}
def dfs(P):
    if P >= C:
        return 0
    elif P in memo:
        return memo[P]
    tem = []
    for money, person in city:
        tem.append(money + dfs(P+person))
    if len(tem)==0: return sys.maxsize
    memo[P] = min(tem)
    return memo[P]

def solution(C,N,city):
    dfs(0)
    return memo[0]

print(solution(C,N,city))
