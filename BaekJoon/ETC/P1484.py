# BaekJoon P1484 "다이어트" (수학, 정수론, 투포인터 | G5)
"""
---[실수]---
출력 부분 실수
---[부족한 점]---
---[풀이]---
real -> 실제 몸무게
thought -> 예상 몸무게
두 값의 제곱의 차가 G보다 작다면
real을 키워 차이를 키우고
크다면
thought을 키워 차이를 줄임
---[비고]---
"""
import sys
input = sys.stdin.readline


def solution(g):
    answer = []
    real = 1
    thought = 1
    while real < 100000 and thought < 100000:
        result = real ** 2 - thought ** 2
        if result == g:
            answer.append(real)
            real += 1
            thought += 1

        elif result < g:
            real += 1
        else:
            thought += 1

    return answer


if __name__ == '__main__':
    G = int(input())
    answer = solution(G)
    print(*answer if len(answer) != 0 else [-1], sep='\n')
