# BaekJoon P12904 A와B (백트래킹 | Gold5)
"""
[실수]
백트래킹을 생각했지만, 동일할거라고 생각해버리고 넘어감
결론은 백트래킹

[부족한 점]
깊게 생각하지 않고 무작정 문제풀이로 들어간 듯

[풀이]
백트래킹.
S -> T 가 아닌
T -> S 로 변경하는 것
이 떄 중요한 것은 맨 뒤에 있는 문자에 대한 경우만 처리해 주면 됨
차피 규칙에 따라 T -> S 가 가능한지만 확인하면 됨. 즉, 모든 경우를 다 볼 필요가 없다는 것
ex) T == ABAAB : 맨 뒤 문자가 B 이므로 AABA를 reverse하고 B를 붙였겠구나 로 판단
    => AABA : 맨 뒤 문자가 A 이므로 AAB에서 A를 붙였겠구나로 판단
    => AAB ...

"""
def solution(s,t):
    while s != t:
        if len(s) == len(t):
            return 0
        if t[-1] == 'A':
            t = t[:-1]
        else:
            t = t[:-1]
            t = t[::-1]

    return 1


if __name__ == '__main__':
    s = input()
    t = input()

    print(solution(s,t))
