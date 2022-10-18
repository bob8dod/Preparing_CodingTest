# BaekJoon P2800 "괄호제거" (자료구조, 스택 | G5)
"""
---[실수]---
1. "어떤 식을 여러 쌍의 괄호가 감쌀 수 있다." -> ((1))과 같은 경우를 무시함
    => 결과들을 저장하는 공간을 list 가 아닌 set 으로 설정 -> 중복 제거
---[부족한 점]---
---[풀이]---
---[비고]---
풀이 시간 : 22m
재귀로 푼 사람이 있는지 궁금
"""
from collections import deque
from itertools import combinations


def solution(operation):
    info = []
    stk = deque([])
    for idx, c in enumerate(operation):
        if c == '(':
            stk.append(idx)
        elif c == ')':
            info.append([stk.pop(), idx])

    answer = set()
    for step in range(1,len(info)+1):
        for choiced in combinations(info,step):
            temp = list(operation)
            for first, end in choiced:
                temp[first] = temp[end] = ''
            answer.add(''.join(temp))

    return sorted(answer)

if __name__ == '__main__':
    inputs = input()
    print(*solution(inputs), sep='\n')
