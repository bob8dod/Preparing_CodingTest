# 1로 만들기 최적화 ver1
"""
동적프로그래밍.
계산된 놈들을 따로 저장해두어서 다시 사용하는 방법
tem을 구하는 과정에서 min을 통해서 바로 최소값을 구하도록 유도
+x%2, +x%3 은 '-1 행동'을 표현한것 -> 중요
"""
memo={1:0, 2:1}
def calc(x):
    if x in memo: return memo[x]
    tem = 1 + min(calc(x//2)+x%2, calc(x//3)+x%3)
    memo[x] = tem
    return tem

print(calc(int(input())))
