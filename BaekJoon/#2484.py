# 주사위 네개
"""
입력 받은 dice들에 대해서
개수를 직접 세어 dictionary로 표현,
그 결과를 통해 계산 진행
"""

from collections import defaultdict

def solution():
    result = 0
    N = int(input())
    for i in range(N):
        dice = list(map(int, input().split()))
        temp = cal(dice)
        if temp > result:
            result = temp
    return result

def cal(dice):
    dict_dice = defaultdict(int)
    for i in dice:
        dict_dice[i] += 1

    if len(dict_dice.keys()) == 1:
        return 50000 + dice[0]*5000
    elif len(dict_dice.keys()) == 2:
        for i in dict_dice.keys():
            if dict_dice[i] == 3:
                return 10000 + i*1000
            if dict_dice[i] == 2:
                return 2000 + sum(dict_dice.keys())*500
    elif len(dict_dice.keys()) == 3:
        for i in dict_dice.keys():
            if dict_dice[i] == 2:
                return 1000 + i*100
    else:
        return max(dict_dice.keys())*100

print(solution())
