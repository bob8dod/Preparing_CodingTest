#행운의 문자열
"""
일단 해당 문자열에서 문자들이 각각 얼마나 나온지 Count로 측정
결과의 dict를 이용해서 dfs를 통해 가지를 내리며 가능한 경우를 측정
이때 즉, 가지를 내릴 시 현재 노드를 제외하고 모든 노드가 0 or 1이면
그냥 거기서 팩토리얼 계산 때려버림
여기서 중요한 것은 얘가 가지를 내릴지 안내릴지 판단하는 부분에서
가지를 내린다면 dict에서 해당 문자에 대한 count를 -1 해주는데
이 dict는 공유되고 있기에 가지를 내리고 돌아올 때 다시 count를 +1 해줌으로써
그 층에서의 dict를 복원해줘야 함. -> dfs이므로
"""

from collections import Counter
from math import factorial

def dfs(i, s):
    global result
    if i == len(S):
        result += 1
        return

    if len(s)==0 or s_dict[s] == 0:
        cnt = 0
        flag = True
        for j in s_dict.values():
            if j == 0:
                continue
            if j == 1:
                cnt += 1
            else:
                flag = False
                break
        if flag:
            result += factorial(cnt)
            return

    for c in s_dict.keys():
        if s_dict[c] == 0:
            continue
        if len(s)==0:
            s_dict[c] -= 1
            dfs(i + 1, c)
            s_dict[c] += 1
        elif s != c:
            s_dict[c] -= 1
            dfs(i + 1, c)
            s_dict[c] += 1


def solution(S):
    global result, s_dict
    s_dict = Counter(S)
    result = 0
    dfs(0,'')

    return result


S = input()
print(solution(S))
