# 42895 N으로 표현
"""
dfs로 푼 버전.
현재 상태에서 가능한 모든 사친연산과 연산에 사용되는 숫자를 모두 고려한 상황.
즉, +,-,//,* 와 N, NN, NNN, NNNN (cnt에 혀용되는 볌위내의 숫자 이어붙이기) 의 모든 조합을 탐색/
"""

import sys

N = None
number = None
answer = sys.maxsize

def dfs(res, cnt):
    global answer
    if res == number: answer = min(answer, cnt)
    if cnt > 8 : return

    for i in range(1, 9-cnt):
        tem = int(str(N)*i)
        dfs(res + tem, cnt + i)
        dfs(res - tem, cnt + i)
        dfs(res // tem, cnt + i)
        dfs(res * tem, cnt + i)

def solution(a,b):
    global N, number
    N, number = a, b
    dfs(0,0)
    if answer == sys.maxsize: return -1
    return answer

print(solution(2,11))
