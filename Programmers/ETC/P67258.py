# 프로그래머스 2020 카카오 인턴십 Two Pointer, Window P67258 보석 쇼핑
"""
투포인터로 진행.
가장 먼저 해당 조건(모든 종류의 보석을 적어도 1개 이상 포함)을 만족할 때 까지 end pointer를 펼치고
그 후 start pointer를 옮겨 구간을 줄여가며 가장 짧은 구간을 측정
이 짓을 계속해서 반복하는 것!
즉, 개수가 부족하면 e를 늘리고, 개수가 맞으면 s를 늘리면서 윈도우를 옮기는 것
"""
import sys
from collections import defaultdict


def solution(gems):
    cri = len(set(gems))
    memo = defaultdict(int)

    length = sys.maxsize
    s, e = 0, 0
    answer = [s + 1, e + 1]

    memo[gems[e]] += 1
    while True:
        if len(memo) != cri:
            e += 1
            if e == len(gems): break
            memo[gems[e]] += 1
        else:
            if length > e - s + 1:
                length = e - s + 1
                answer = [s + 1, e + 1]
            memo[gems[s]] -= 1
            if memo[gems[s]] == 0:
                del memo[gems[s]]
            s += 1
            if s > e: break

    return answer


print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
