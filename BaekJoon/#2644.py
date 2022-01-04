# 촌수계산(tree, graph)_40min
"""
먼저 지정된 노드의 모든 조상을 구한 후
그 조상들 중 공통 조상이 존재하는 지, 그 조상까지의 거리가 얼마인지
계산하고 더한 값을 반환
"""
gra = {}
def check(a,b):
    li_a = [a]
    li_b = [b]
    tem_a = a
    tem_b = b
    while True:
        if tem_a not in gra and tem_b not in gra: break
        if tem_a in gra:
            tem_a = gra[tem_a]
            li_a.append(tem_a)
        if tem_b in gra:
            tem_b = gra[tem_b]
            li_b.append(tem_b)

    if not set(li_a)&set(li_b): return -1
    for i in range(len(li_a)):
        for j in range(len(li_b)):
            if li_a[i] == li_b[j]: return i+j

def solution():
    n = int(input())
    a,b = map(int, input().split())
    k = int(input())
    for i in range(k):
        c, d = map(int, input().split())
        gra[d] = c

    return check(a,b)
