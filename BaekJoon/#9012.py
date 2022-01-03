# 괄호 _ 20min
"""
stack을 이용하여 괄호 체크
( 가 들어올 경우 판단할 것이 없고 바로 추가해줌
) 가 들어올 경우 2가지로 판단.
"""

import sys

def check(li):
    if len(li) % 2 != 0: return 'NO'
    st = []
    for i in li:
        if i == '(':
            st.append(i)
        else:
            if len(st) == 0: return 'NO'
            st.pop()
    return 'YES' if len(st) == 0 else 'NO'

def solution():
    N = int(input())
    result = []
    for i in range(N):
        li = sys.stdin.readline().strip()
        result.append(check(li))
    return result
