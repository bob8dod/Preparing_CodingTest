# BaekJoon P1991 "트리 순회" (트리, 재귀| S1)
"""
---[실수]---
---[부족한 점]---
아직도 재귀의 반환값을 유연하게 처리하지 못함.
global 로 풀어버리고 싶음
---[풀이]---
각각의 조각들을 순서에 맞게 합쳐준다고 생각하면 됨
전위 순회 - 자기 자신을 가장 먼저 합쳐줌
중위 순회 - 자기 자신을 중간에 합쳐줌
후위 순회 - 자기 자신을 가장 마지막에 합쳐줌
% result += curr 의 위치 차이.
---[비고]---
풀이시간: 22m
메모리: 30840 | 시간: 68
"""
import sys


def pre_order(curr, info):
    if curr == '.':
        return ''

    result = ''
    left, right = info[curr]

    result += curr
    result += pre_order(left, info)
    result += pre_order(right, info)

    return result


# 카카오 문제에서 중위순회을 이용해야 되는 문제가 있었던 거 같음
# 트리를 아래로 누른 후 일자로 쭉 늘린 형태의 모습
def in_order(curr, info):
    if curr == '.':
        return ''

    result = ''
    left, right = info[curr]

    result += in_order(left, info)
    result += curr
    result += in_order(right, info)

    return result


def post_order(curr, info):
    if curr == '.':
        return ''

    result = ''
    left, right = info[curr]

    result += post_order(left, info)
    result += post_order(right, info)
    result += curr

    return result


def solution(n, graph):
    info = {}
    for parent, left, right in graph:
        info[parent] = [left, right]

    answer = []
    answer.append(pre_order('A', info))
    answer.append(in_order('A', info))
    answer.append(post_order('A', info))
    return answer


if __name__ == '__main__':
    N = int(input())
    inputs = [[*sys.stdin.readline().split()] for _ in range(N)]
    print(*solution(N, inputs), sep='\n')
