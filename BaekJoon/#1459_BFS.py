# 기타리스트
"""
BFS로 푼 버전.
하지만 BFS로 풀면 128MB의 메모리 제한을 초과하게 됨
BFS는 
범위 안에만 있다면 뿌리를 내리고
마지막 층(맨 아래 층, 결과적으로 가능한 놈들이 모인 층)에서 가장 큰 놈을 선택
마지막 층에 요소가 없다면 -1 출력
"""

from collections import deque
result = []

N,S,M = map(int, input().split())
li = list(map(int, input().split()))

def bfs():
    Q = deque([[S,0]])
    while Q:
        curr, i = Q.popleft()
        if i == len(li):
            result.append(curr)
            continue
        left = curr - li[i]
        right = curr + li[i]
        if left >= 0: Q.append([left,i+1])
        if right <= M: Q.append([right,i+1])


def solution():
    bfs()
    if len(result) == 0: return -1
    return max(result)

print(solution())
