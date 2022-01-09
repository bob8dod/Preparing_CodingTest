# 친구 최적화
"""
먼저 주어진 metrix에 따라 각 사람별 1-친구 목록을 people이라는 dict에 set으로 만들어줌
문제에 주어진 조건을 달리 생각하여
결국 친구의 친구는 나의 2-친구에 포함된다는 개념을 이용해서
각 사람의 친구의 1-친구들을 모두 포함해줌. -> 2-친구 목록
set을 통해 겹치는 친구들은 자동으로 처리.
"""

from collections import defaultdict
f_map = []
people = defaultdict(set)

def f_find():
    result = 0
    for i in range(N):
        tem_s = people[i].copy()
        for j in people[i]:
            tem_s.update(people[j])
        result = max(result,len(tem_s)-1)

    return result

def solution():
    global N
    N = int(input())
    for _ in range(N):
        f_map.append(list(input()))

    for i in range(N):
        for j in range(N):
            if f_map[i][j] == 'Y': people[i].add(j)

    print(f_find())
    return
