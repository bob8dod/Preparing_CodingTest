# 1로 만들기 최적화 ver2
"""
그 순간에 선택할 수 있는 모든 경우의 수(4가지)를 따져서
min을 통해 그 선택의 순간에 최소값을 선택하도록 유도
"""

memo={1:0, 2:1, 3:1}
def calc(x):
    if x in memo: return memo[x]
    # case1 : 2랑 3모두로 나누어지는 경우
    if x%6==0: temp = min(calc(x//3),calc(x//2))
    # case2 : 3으로 나누어지는 경우
    elif x%3==0: temp = min(calc(x//3),calc(x-1))
    # case3 : 2로 나누어지는 경우
    elif x%2==0: temp = min(calc(x//2),calc(x-1))
    # 마지막
    else: temp = calc(x-1)
    memo[x] = 1 + temp
    return memo[x]

def solution():
    x = int(input())
    print(calc(x))
