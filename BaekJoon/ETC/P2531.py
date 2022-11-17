# BaekJoon P2531 "회전초밥" (전수조사, 투포인터 | S1)
"""
---[실수]---
---[부족한 점]---
---[풀이]---
쿠폰에 해당하는 초밥을 배제하면서 투포인터 진행 (쿠폰에 해당하는 초밥이 아닐 경우에 대해서만 count 조정)
먼저 보는 범위가 고정되어 있기 때문에 그에 따른 처음 초기 dict 를 설정해주고
정해진 범위를 옮기면서 빼는 초밥이 빠짐으로써 해당 종류가 아예 없으면 cnt -= 1
                  새로 들어온 초밥이 아예 새로운 종류면 +1
각 범위마다 최대 종류의 개수를 기록하고
마지막에 공짜로 먹을 수 있는 초밥 1개를 추가하며 반환환
--[비고]---
풀이시간: 19m
메모리: 32452 | 시간: 120
"""
import sys
from collections import defaultdict


def solution(n, d, k, coupon, sushi_li):
    info = defaultdict(int)
    cnt = 0
    for i in range(k):
        sushi = sushi_li[i]
        if sushi != coupon:
            info[sushi] += 1
            if info[sushi] == 1:
                cnt += 1

    s = 1
    answer = 0
    while s < n:

        # del sushi
        del_sushi = sushi_li[s-1]
        if del_sushi != coupon:
            info[del_sushi] -= 1
            if info[del_sushi] == 0:
                cnt -= 1

        # add sushi
        e = (s + k - 1) % n
        add_sushi = sushi_li[e]
        if add_sushi != coupon:
            info[add_sushi] += 1
            if info[add_sushi] == 1:
                cnt += 1

        s += 1

        answer = max(answer, cnt)


    return answer+1


if __name__ == '__main__':
    N, D, K, C = map(int, input().split())
    inputs = [int(sys.stdin.readline().strip()) for _ in range(N)]
    print(solution(N, D, K, C, inputs))
