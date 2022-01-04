# 촌수 계산 최적화
"""
기존의 코드와 큰 차이는 없음
최적화라기 보다는 좀 더 단순하게 접근한 케이스
"""

def check(a,b,p):
    Ap, Bp = [(a,0)], [(b,0)]
    Ac, Bc = 0, 0
    while p[a] != 0:
        a = p[a]
        Ac += 1
        Ap.append((a, Ac))
    while p[b] != 0:
        b = p[b]
        Bc += 1
        Bp.append((b, Bc))

    print(Ap, Bp)
    for i in Ap:
        for j in Bp:
            if i[0]==j[0]: return i[1]+j[1]
    else: return -1

def solution():
    n = int(input())
    a, b = map(int, input().split())
    p = [0 for _ in range(n+1)]
    k = int(input())
    for _ in range(k):
        x, y = map(int, input().split())
        p[y] = x
    return check(a,b,p)
