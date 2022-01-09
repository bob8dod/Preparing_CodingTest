# 친구 _ 18min
"""
먼저 주어진 metrix에 따라 각 사람별 1-친구 목록을 people이라는 dict에 set으로 만들어줌
그 후 모든 사람을 훑으며 서로가 친구인지 먼저 판단,
아니면 공통 친구가 있는지 set으로 판단
결과를 max로 최댓값 반환
"""

from collections import defaultdict
f_map = []
people = defaultdict(set)

def f_find():
    result = [0 for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j: continue
            if j in people[i]: result[i] +=1
            elif people[i] & people[j]: result[i] +=1

    return max(result)

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

solution()
