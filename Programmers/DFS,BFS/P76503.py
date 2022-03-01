# 프로그래머스 월간 코드 챌린지 시즌2 P76503 모두 0으로 만들기
"""
트리라는 점에서 착안하여 
어떤 노드가 root가 되든 결과가 똑같은 것을 인지했고,
leaf노드들 부터 0을 만들어 root까지 가면 되겠다 생각하고
노드들을 0으로 만들 때 쓰인 값들을 상위 노드들에게 넘겨주며
그 값을 누적.
"""

import sys
sys.setrecursionlimit(300000)

answer = 0

def dfs(i):
    global answer

    visited[i] = 1
    cal = 0
    for next in gmap[i]:
        if not visited[next]:
            cal += dfs(next)

    a[i] = a[i] + cal
    answer += abs(a[i])
    return a[i]



def solution(_, edges):
    global visited, a, gmap
    a = _

    visited = [0 for _ in range(len(a))]
    if sum(a) != 0:
        return -1

    gmap = [[] for _ in range(len(a))]
    for b,c in edges:
        gmap[b].append(c)
        gmap[c].append(b)

    dfs(0)
    return answer

print(solution([-5,0,2,1,2], 	[[0,1],[3,4],[2,3],[0,3]]))
