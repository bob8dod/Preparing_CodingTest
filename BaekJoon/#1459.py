# 기타리스트
"""
!! 좀 특이한 케이스이므로 중요 !!
BFS/DFS로 풀면 메모리 초과로 오답으로 처리됨
이 문제는 DP로, 모든 경우에 대해 행렬로 만들어주고
(이때의 행렬은 (N+1)*(M+1). 즉, 열은 트리의 층이라고 생각하면되고 행은 0(최소)~M(최대) 까지의 값, 결국 가능한 모든 경우에 대한 행렬)
각각의 값들이 해당 되는지 True or False로 표시하며 다음단계로 넘어간다고 생각하면 됨
(int형 자료를 넣어도 메모리 초과가 안남. 결국 하나의 행렬을 만들어서 그걸 가지고 놀아야 메모리 초과가 안나는듯)
다 구해졌으면 이제 table의 마지막 행 중 가장 큰놈이 구하면 됨
"""

def solution(N,S,M,li):
    table = [[False for _ in range(M+1)] for _ in range(N+1)]
    table[0][S] = True
    for i in range(N):
        for j in range(M+1):
            if table[i][j]:
                curr = j
                left = curr - li[i]
                right = curr + li[i]
                if left >= 0: table[i+1][left] = True
                if right <= M: table[i+1][right] = True

    answer = -1
    for idx, val in enumerate(table[-1][::-1]):
        if val:
            answer = M-idx
            break

    return answer


N,S,M = map(int,input().split())
li = list(map(int,input().split()))
print(solution(N,S,M,li))
