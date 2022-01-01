# 1로 만들기
"""
먼저 Tree형식이라고 생각했을 때,
가능한 모든 경우를 search하지만
현재 cnt가 지금까지 나온 최소 cnt보다 같거나 큰 경우 (즉, 더 깊이 들어가는 경우) 종료
-> 약간 가지치기 느낌
현재 cnt가 작은 경우에서 1이 나오면 min_cnt 변경
이런 식으로 serach.
"""
def calc(X, cnt):
    global min_cnt
    if cnt >= min_cnt: return
    if X == 1:
        min_cnt = cnt
        return
    if X % 3 == 0: calc(X // 3, cnt + 1)
    if X % 2 == 0: calc(X // 2, cnt + 1)
    calc(X - 1, cnt + 1)

def solution():
    X = int(input())
    global min_cnt
    min_cnt = X
    calc(X, 0)
    print(min_cnt)

solution()
