#행운의 문자열
from collections import Counter
from math import factorial

def dfs(i, s):
    global result
    if i == len(S):
        result += 1
        return

    for c in s_dict.keys():
        if s_dict[c] == 0:
            continue
        if len(s)==0:
            s_dict[c] -= 1
            dfs(i + 1, c)
            s_dict[c] += 1
        elif s != c:
            # if sum([1 for i in s_dict.items() if i[1] == 1]) == len(s_dict):
            #     result += factorial()
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
