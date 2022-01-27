# 추월 _ 20min
"""
터널에서 나오는 차들의 순서를 기록한 out_cars 기준으로
맨 나중의 순서부터 reverse해서 확인.
확인 시 기준이 되는 car보다 in_cars에서는 뒷순위인데 앞에 있을 경우,
result라는 집합에 저장.
결국 result에는 총 추월한 차들이 기록됨
"""
import sys

N = int(input())
in_cars = {sys.stdin.readline().strip():i for i in range(N)}
out_cars = [sys.stdin.readline().strip() for i in range(N)]


def solution(N, in_cars, out_cars):
    result = set()
    for i, val1 in enumerate(reversed(out_cars)):
        for j, val2 in enumerate(reversed(out_cars)):
            if i >= j: continue
            if in_cars[val1] < in_cars[val2]: result.add(val2)
    return len(result)

print(solution(N, in_cars, out_cars))
