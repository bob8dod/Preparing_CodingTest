"""
받아온 dice list를 정렬하여 판단. -> 훨씬 효율적
정렬을 통해 판단하면 훨씬 편함 -> 어차피 dice의 가짓수는 6가지!
"""
def calc():
    dice = sorted(map(int, input().split()))
    # case 1
    if len(set(dice)) == 1: return dice[0]*5000 + 50000
    # case 2
    if len(set(dice)) == 2:
        if dice[1] == dice[2]: return dice[1]*1000 + 10000
        # case 3
        return (dice[1] + dice[2])*500 + 2000
    # case 4
    for i in range(3):
        if dice[i] == dice[i+1]: return dice[i]*100 + 1000
    # case 5
    return dice[-1] * 100

def solution():
    N = int(input())
    return max(calc() for i in range(N))

print(solution())
