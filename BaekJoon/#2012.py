# 등수 매기기 _ 17min
"""
예상 등수를 정렬한 후
해당 순서에 맞게 실제 등수를 부여
이렇게 하면 최소 불만도(|예상-실제|)가 됨.
여기서 중요한 부분은 input() 대신 sys.stdin.readline().strip()
"""
import sys

def check(score):
    degree = 0
    for idx, val in enumerate(sorted(score)):
        degree += abs(val-idx)

    return degree

def solution():
    score=[0]
    N = int(input())
    for i in range(N):
        score.append(int(sys.stdin.readline().strip()))
    
    return check(score)
