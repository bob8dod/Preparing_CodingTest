from sys import stdin, maxsize
"""
DP로 푼 버전.
각 city의 정보를 기준으로 그 때의 조건들을 이용해서 DP를 업데이트함.
(기존에 저장된 DP의 cost와 현재 계산하는 DP의 cost 중 더 작은 값을 선택하여 업데이트)
그렇게 되면 기존의 city 정보들이 누적된 상태로 DP를 최적화한 상태라
새로운 city 정보로 DP를 업데이트할 때, 결론적으로 각 Person에서의 
모든 city 정보를 고려한 최소 Cost로 저장됨.
"""
# 확보해야할 고객, 도시의 수
C, N = map(int, stdin.readline().split())
# 광고 정보
ad = [list(map(int, stdin.readline().split())) for _ in range(N)]
# 적어도 C명을 늘려야 하기에, 고객의 수 최대 값을 더해 줄 필요가 있음
dp = [0] + [maxsize] * (C + 100)

for cost, customer in ad:
    for cur_customer in range(customer, C + 101):
        dp[cur_customer] = min(dp[cur_customer], dp[cur_customer - customer] + cost)

print(min(dp[C:]))
