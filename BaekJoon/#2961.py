# 2961 도영이가 만든 맛있는 음식 _ 19mins
"""
가능한 모든 조합을 찾아내어
모두 계산해 놓은 뒤 가장 작은 값을 도출
"""
from itertools import combinations

N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]

def soltion(n, li):
    result = []
    for i in range(1, len(li)+1):
        for c in combinations(li, i):
            total_sum = 0
            total_mul = 1
            for j in c:
                total_mul *= j[0]
                total_sum += j[1]
            result.append(abs(total_mul - total_sum))

    return min(result)


print(soltion(N, li))
