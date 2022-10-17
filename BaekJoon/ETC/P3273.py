# BaekJoon P3273 "두수의 합" (정렬, 투 포인터 | S3)
"""
---[실수]---
---[부족한 점]---
---[풀이]---
---[비고]---
풀이 시간 : 11m
"""
import sys


def solution(numbers, x):
    numbers.sort()
    num_set = set(numbers)
    mid = x//2

    answer = 0
    for n in numbers:
        if n > mid : break
        target = x - n
        if target != n and target in num_set:
            answer += 1

    return answer

if __name__ == '__main__':
    N = int(input())
    inputs = [*map(int, sys.stdin.readline().split())]
    X = int(input())
    print(solution(inputs, X))
