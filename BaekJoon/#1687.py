# 숨바꼭질 _ 60min
"""
bfs로 푸는 것을 인지한 상태로 풀었으나 time을 구하는 데에 있어서 오래걸림
ch 이라는 dict를 생성해서 해당 tree에서의 "층"을 기록함과 동시에 visited까지 구현
해당 숫자의 층을 기록하는 것이 핵심. 이걸 구현하지 못했음
또한 해당 숫자의 x-1 x+1 x*2 의 결과의 범위가 1000000이하인지를 판단하지 않으면 메로리 초과로 오류
이 부분에 있어서도 시간이 오래걸림
-> 해주어야 할 부분은 하나도 놓치지 말고 해주기!
"""
from collections import deque
Q = deque()
ch = {}

def bfs(n,k):
    Q.append(n)
    ch[n] = 0
    while True:
        x = Q.popleft()
        if x == k: return ch[x]
        for i in [x-1,x+1,x*2]:
            if 0 <= i <= 1000000 and i not in ch:
                Q.append(i)
                ch[i] = ch[x]+1

def solution():
    N, K = map(int, input().split())
    return bfs(N,K)
