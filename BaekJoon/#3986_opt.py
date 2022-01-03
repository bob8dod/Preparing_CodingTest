# 좋은 단어 최적화
"""
stack을 사용하지 않고 문자열 그대로 판단
AA 와 BB를 빈문자열로 대체 함으로써 반복적으로 판단
"""

def check(li):
    while li:
        tem1 = li.replace('AA','')
        tem2 = tem1.replace('BB','')
        if tem2 == li: return 0
        li = tem2

    return 1

def solution():
    N = int(input())
    result = 0
    for _ in range(N):
        li = input()
        result += check(li)

    return result
