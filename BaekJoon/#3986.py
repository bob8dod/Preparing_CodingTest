# 좋은 단어_20min
"""
stack을 통해 판단
해당 문자에서 stack이 비었거나 stack.top이 다른 문자일 경우 그냥 추가
다른 모든 경우에 pop진행
이게 좋은 단어인지 판단하는 것은 가장 나중에 진행
"""

def check(li):
    if len(li)%2 != 0: return 0
    st = []
    for i in li:
        if len(st)==0 or st[-1]!=i : st.append(i)
        else: st.pop()

    return 1 if len(st)==0 else 0

def solution():
    N = int(input())
    result = 0
    for _ in range(N):
        li = input()
        result += check(li)

    return result
