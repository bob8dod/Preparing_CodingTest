# 2021 Dev-Matching Back-Tracking P77486 다단계 칫솔 판매
"""
가장 먼저 주어진 정보들을 통해 해당 node의 parent가 누군지 저장해 두고
주어진 seller와 amount를 가지고 dfs를 돌림
dfs 시 현재 node와 이 node가 받을 금액을 받아
현재 node의 이익에 money를 10프로 때고 더해줌
그 후 줘야 하는 금액을 parent와 함께 dfs로 보내며 백트리킹 진행.
이떄, 주어진 금액이 0이거나 현재 노드가 center(-) 일 경우 백트래킹 stop.
"""
import sys
sys.setrecursionlimit(100000)

def dfs(curr,money):
    global result

    if curr == '-' or money==0: return

    give = int(money*0.1)
    if give < 1: give = 0
    own = money - give
    result[curr] += own
    
    dfs(gmap[curr], give)


def solution(enroll, referral, seller, amount):
    global result, gmap
    result = {e:0 for e in enroll}
    gmap = {}
    for en, re in zip(enroll,referral):
        gmap[en] = re

    for se,mo in zip(seller,amount):
        dfs(se,mo*100)

    return [v for k, v in result.items()]
