# BaekJoon P1991 "트리순회" (트리, 재귀 | S1)
"""
---[실수]---
---[부족한 점]---
---[풀이]---
---[비고]---
"""

import sys

def pre_order(curr, info):
    if curr == '.':
        return

    left, right = info[curr]
    print(curr, end='')
    pre_order(left, info)
    pre_order(right,info)

def in_order(curr, info):
    if curr == '.':
        return

    left, right = info[curr]
    in_order(left, info)
    print(curr, end='')
    in_order(right,info)

def post_order(curr, info):
    if curr == '.':
        return

    left, right = info[curr]
    post_order(left, info)
    post_order(right,info)
    print(curr, end='')



def solution(n, graph):
    info = {}
    for parent, left, right in graph:
        info[parent] = [left, right]

    pre_order('A',info)
    print()
    in_order('A',info)
    print()
    post_order('A',info)
    print()

if __name__ == '__main__':
    N = int(input())
    inputs = [[*sys.stdin.readline().split()] for _ in range(N)]
    solution(N, inputs)
